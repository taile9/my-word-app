import csv
import re
from collections import defaultdict
from pathlib import Path
from typing import Dict, List, Tuple


ROOT = Path(__file__).resolve().parents[1]
DATA1 = ROOT / "public" / "data.csv"
DATA2 = ROOT / "public" / "data2.csv"


DAY_RE = re.compile(r"^day\s*(\d+)$", re.IGNORECASE)


def norm(s: str) -> str:
    return (s or "").strip().replace("\ufeff", "")


def parse_tsv_lines(path: Path) -> List[List[str]]:
    text = path.read_text(encoding="utf-8").replace("\r", "")
    rows: List[List[str]] = []
    for raw_line in text.split("\n"):
        if not raw_line.strip():
            continue
        rows.append(raw_line.split("\t"))
    return rows


def is_word_row_data2(parts: List[str]) -> Tuple[bool, int, str, str]:
    """
    data2.csv (after rebuild) is normalized as:
      - Word row:   dayN <tab> word/expression <tab> meaning
      - Example row: <tab> exampleEng <tab> exampleKor
    So we treat any dayN row with non-empty word+meaning as a word row,
    even if the meaning ends with '.'.
    """
    day_col = norm(parts[0]) if len(parts) >= 1 else ""
    m = DAY_RE.match(day_col)
    if not m:
        return False, 0, "", ""
    day = int(m.group(1))
    eng = norm(parts[1]) if len(parts) >= 2 else ""
    kor = norm(parts[2]) if len(parts) >= 3 else ""
    if not eng or not kor:
        return False, 0, "", ""
    return True, day, eng, kor


def is_word_row_data1(parts: List[str]) -> Tuple[bool, int, str, str]:
    day_col = norm(parts[0]) if len(parts) >= 1 else ""
    m = DAY_RE.match(day_col)
    if not m:
        return False, 0, "", ""
    day = int(m.group(1))
    eng = norm(parts[1]) if len(parts) >= 2 else ""
    kor = norm(parts[2]) if len(parts) >= 3 else ""
    if not eng or not kor:
        return False, 0, "", ""
    return True, day, eng, kor


def build_day_map(path: Path, which: str) -> Dict[int, List[str]]:
    rows = parse_tsv_lines(path)
    out: Dict[int, List[str]] = defaultdict(list)
    for parts in rows:
        if which == "data2":
            ok, day, eng, _kor = is_word_row_data2(parts)
        else:
            ok, day, eng, _kor = is_word_row_data1(parts)
        if ok:
            out[day].append(eng)
    return out


def main() -> None:
    d1 = build_day_map(DATA1, "data1")
    d2 = build_day_map(DATA2, "data2")

    print("=== Day counts (data.csv vs data2.csv) ===")
    for day in range(1, 31):
        c1 = len(d1.get(day, []))
        c2 = len(d2.get(day, []))
        flag = ""
        if c1 != c2:
            flag = "  <<DIFF>>"
        print(f"day{day}: data.csv={c1:>3} | data2.csv={c2:>3}{flag}")

    print("\n=== Missing/Extra words by day (based on word rows) ===")
    for day in range(1, 31):
        s1 = set(d1.get(day, []))
        s2 = set(d2.get(day, []))
        missing = sorted(s1 - s2)
        extra = sorted(s2 - s1)
        if not missing and not extra:
            continue
        print(f"\n--- day{day} ---")
        if missing:
            print(f"MISSING in data2 ({len(missing)}): " + ", ".join(missing))
        if extra:
            print(f"EXTRA in data2   ({len(extra)}): " + ", ".join(extra))


if __name__ == "__main__":
    main()

