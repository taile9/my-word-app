import re
from collections import defaultdict
from dataclasses import dataclass
from pathlib import Path
from typing import Dict, List, Optional, Tuple


ROOT = Path(__file__).resolve().parents[1]
DATA1 = ROOT / "public" / "data.csv"
DATA2 = ROOT / "public" / "data2.csv"

DAY_RE = re.compile(r"^day\s*(\d+)$", re.IGNORECASE)


def norm(s: str) -> str:
    return (s or "").replace("\ufeff", "").strip()


def parse_data1() -> List[Tuple[int, str, str, str, str]]:
    """
    Parse public/data.csv (TSV). Returns list of:
      (day, word, meaning, exEng, exKor)
    Example columns may be missing; then exEng/exKor are ''.
    """
    text = DATA1.read_text(encoding="utf-8").replace("\r", "")
    out: List[Tuple[int, str, str, str, str]] = []
    for raw in text.split("\n"):
        if not raw.strip():
            continue
        parts = raw.split("\t")
        day_col = norm(parts[0]) if len(parts) >= 1 else ""
        m = DAY_RE.match(day_col)
        if not m:
            continue
        day = int(m.group(1))
        word = norm(parts[1]) if len(parts) >= 2 else ""
        meaning = norm(parts[2]) if len(parts) >= 3 else ""
        ex_eng = norm(parts[3]) if len(parts) >= 4 else ""
        ex_kor = norm(parts[4]) if len(parts) >= 5 else ""
        if not word or not meaning:
            continue
        out.append((day, word, meaning, ex_eng, ex_kor))
    return out


def looks_like_sentence(s: str) -> bool:
    s = norm(s)
    if not s:
        return False
    # Has multiple words or ends with sentence punctuation
    if len(s.split()) >= 3:
        return True
    if s.endswith((".", "?", "!")):
        return True
    return False


def extract_examples_from_messy_data2() -> Dict[Tuple[int, str], Tuple[str, str]]:
    """
    Best-effort extraction of examples from the current (messy) data2.csv.
    Keyed by (day, word).
    """
    text = DATA2.read_text(encoding="utf-8").replace("\r", "")
    lines = [ln for ln in text.split("\n") if ln.strip()]

    examples: Dict[Tuple[int, str], Tuple[str, str]] = {}
    cur_day: Optional[int] = None
    cur_word: Optional[str] = None

    for raw in lines:
        parts = raw.split("\t")
        c0 = norm(parts[0]) if len(parts) >= 1 else ""

        day_match = DAY_RE.match(c0)
        if day_match:
            day = int(day_match.group(1))
            c1 = norm(parts[1]) if len(parts) >= 2 else ""
            c2 = norm(parts[2]) if len(parts) >= 3 else ""

            # Word row candidate: has meaning-like Korean (not a full sentence)
            if c1 and c2 and not c2.endswith(".") and not looks_like_sentence(c1):
                cur_day, cur_word = day, c1
                continue

            # Example row that (incorrectly) starts with dayN
            if cur_day is not None and cur_word is not None and c1 and c2 and looks_like_sentence(c1):
                key = (cur_day, cur_word)
                if key not in examples:
                    examples[key] = (c1, c2)
                continue

            # Otherwise ignore
            continue

        # Proper example row: starts with empty first column (leading tab)
        if cur_day is not None and cur_word is not None:
            c1 = norm(parts[1]) if len(parts) >= 2 else ""
            c2 = norm(parts[2]) if len(parts) >= 3 else ""
            if c1 and c2 and looks_like_sentence(c1):
                key = (cur_day, cur_word)
                if key not in examples:
                    examples[key] = (c1, c2)

    return examples


def default_example(word: str) -> Tuple[str, str]:
    return (f"I am studying the word {word}.", f"나는 {word} 단어를 공부하고 있다.")


def rebuild() -> None:
    data1_rows = parse_data1()
    extracted = extract_examples_from_messy_data2()

    out_lines: List[str] = []
    for day, word, meaning, ex_eng_1, ex_kor_1 in data1_rows:
        key = (day, word)
        ex_eng, ex_kor = extracted.get(key, ("", ""))
        if not ex_eng or not ex_kor:
            if ex_eng_1 and ex_kor_1:
                ex_eng, ex_kor = ex_eng_1, ex_kor_1
            else:
                ex_eng, ex_kor = default_example(word)

        out_lines.append(f"day{day}\t{word}\t{meaning}\n")
        out_lines.append(f"\t{ex_eng}\t{ex_kor}\n")

    DATA2.write_text("".join(out_lines), encoding="utf-8")


if __name__ == "__main__":
    rebuild()

