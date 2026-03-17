import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DATA2 = ROOT / "public" / "data2.csv"
DAY_RE = re.compile(r"^day\s*(\d+)$", re.IGNORECASE)


def norm(s: str) -> str:
    return (s or "").replace("\ufeff", "").strip()


def main() -> None:
    text = DATA2.read_text(encoding="utf-8").replace("\r", "")
    lines = [ln for ln in text.split("\n") if ln.strip()]

    issues = []
    word_lines = 0
    example_lines = 0

    i = 0
    while i < len(lines):
        parts = lines[i].split("\t")
        c0 = norm(parts[0]) if len(parts) >= 1 else ""
        if not DAY_RE.match(c0):
            issues.append((i + 1, "Expected dayN word line", lines[i]))
            i += 1
            continue

        if len(parts) < 3 or not norm(parts[1]) or not norm(parts[2]):
            issues.append((i + 1, "Word line missing word/meaning", lines[i]))
        word_lines += 1

        if i + 1 >= len(lines):
            issues.append((i + 1, "Missing example line after word line", lines[i]))
            break

        ex_parts = lines[i + 1].split("\t")
        ex0 = norm(ex_parts[0]) if len(ex_parts) >= 1 else ""
        if ex0 != "":
            issues.append((i + 2, "Example line should start with a leading tab (empty first column)", lines[i + 1]))
        if len(ex_parts) < 3 or not norm(ex_parts[1]) or not norm(ex_parts[2]):
            issues.append((i + 2, "Example line missing exEng/exKor", lines[i + 1]))
        example_lines += 1

        i += 2

    print(f"Word lines: {word_lines}, Example lines: {example_lines}, Total non-empty lines: {len(lines)}")
    if issues:
        print(f"\nISSUES ({len(issues)}):")
        for ln, msg, content in issues[:50]:
            print(f"- L{ln}: {msg} :: {content}")
        if len(issues) > 50:
            print(f"... {len(issues) - 50} more")
    else:
        print("\nOK: data2.csv is consistently (word line + example line) pairs.")


if __name__ == "__main__":
    main()

