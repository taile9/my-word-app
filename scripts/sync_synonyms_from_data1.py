import re
from pathlib import Path
from typing import Dict, List, Optional, Tuple


ROOT = Path(__file__).resolve().parents[1]
DATA1 = ROOT / "public" / "data.csv"
DATA2 = ROOT / "public" / "data2.csv"

DAY_RE = re.compile(r"^day\s*(\d+)$", re.IGNORECASE)
PAREN_RE = re.compile(r"\(([^)]*)\)")

# A loose detector: english token + korean token pairs inside parentheses.
PAIR_RE = re.compile(r"([A-Za-z][A-Za-z'’-]*)\s*([가-힣][가-힣\s]+)")


def norm(s: str) -> str:
    return (s or "").replace("\ufeff", "").strip()


def extract_synonyms_from_meaning(meaning: str) -> Tuple[str, str]:
    """
    From data.csv meaning field, split out synonym info ONLY when parentheses contain
    (english+korean) pairs like: (foresee예견하다, oversea해외의)

    Returns (clean_meaning, synonyms_text)
      - clean_meaning: meaning with that synonym-parentheses removed (and extra spaces trimmed)
      - synonyms_text: lines "eng - kor" joined by '\n'
    """
    m0 = norm(meaning)
    if not m0:
        return "", ""

    synonym_lines: List[str] = []
    remove_spans: List[Tuple[int, int]] = []

    for paren_match in PAREN_RE.finditer(m0):
        inside = paren_match.group(1).strip()
        if not inside:
            continue

        # Only treat as synonyms if there is at least one english+korean pair
        pairs = []
        for eng, kor in PAIR_RE.findall(inside):
            eng2 = norm(eng)
            kor2 = norm(kor)
            if eng2 and kor2:
                pairs.append((eng2, kor2))

        if not pairs:
            continue

        # Heuristic: if inside also contains obvious Korean-only grammar markers like "조건을"
        # without any english word, we'd have no pairs anyway. So safe here.
        for eng2, kor2 in pairs:
            synonym_lines.append(f"{eng2} - {kor2}")

        remove_spans.append((paren_match.start(), paren_match.end()))

    if not synonym_lines:
        return m0, ""

    # Remove synonym parentheses from meaning (from back to front)
    cleaned = m0
    for start, end in reversed(remove_spans):
        cleaned = cleaned[:start] + cleaned[end:]

    cleaned = re.sub(r"\s{2,}", " ", cleaned).strip()
    return cleaned, "\n".join(dict.fromkeys(synonym_lines))  # de-dupe while preserving order


def parse_data1_map() -> Dict[Tuple[int, str], Tuple[str, str]]:
    """
    Returns (day, word) -> (cleanMeaning, synonymsText)
    """
    text = DATA1.read_text(encoding="utf-8").replace("\r", "")
    out: Dict[Tuple[int, str], Tuple[str, str]] = {}
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
        if not word or not meaning:
            continue
        clean_meaning, syn = extract_synonyms_from_meaning(meaning)
        out[(day, word)] = (clean_meaning or meaning, syn)
    return out


def main() -> None:
    # data2 is normalized as pairs of lines
    text2 = DATA2.read_text(encoding="utf-8").replace("\r", "")
    lines = [ln for ln in text2.split("\n") if ln.strip() != ""]

    m1 = parse_data1_map()

    out_lines: List[str] = []
    updated = 0
    missing_map = 0

    i = 0
    while i < len(lines):
        word_parts = lines[i].split("\t")
        day_col = norm(word_parts[0]) if len(word_parts) >= 1 else ""
        m = DAY_RE.match(day_col)
        if not m:
            # pass-through
            out_lines.append(lines[i] + "\n")
            i += 1
            continue

        day = int(m.group(1))
        word = norm(word_parts[1]) if len(word_parts) >= 2 else ""
        meaning = norm(word_parts[2]) if len(word_parts) >= 3 else ""

        ex_line = lines[i + 1] if i + 1 < len(lines) else ""

        key = (day, word)
        if key in m1:
            clean_meaning, syn = m1[key]
            # keep existing meaning if data1 meaning is empty (shouldn't)
            final_meaning = clean_meaning or meaning
            syn_cell = syn.replace("\n", "\\n") if syn else ""
            out_lines.append(f"day{day}\t{word}\t{final_meaning}\t{syn_cell}\n")
            out_lines.append(ex_line + "\n")
            if syn:
                updated += 1
        else:
            missing_map += 1
            out_lines.append(lines[i] + "\n")
            out_lines.append(ex_line + "\n")

        i += 2

    DATA2.write_text("".join(out_lines), encoding="utf-8")
    print(f"Synonym rows added/updated: {updated}")
    print(f"Missing mapping entries: {missing_map}")


if __name__ == "__main__":
    main()

