import hashlib
import re
from pathlib import Path
from typing import List, Tuple


ROOT = Path(__file__).resolve().parents[1]
DATA2 = ROOT / "public" / "data2.csv"

DAY_WORD_RE = re.compile(r"^(day\d+)\t([^\t]+)\t([^\t]+)\s*$", re.IGNORECASE)


def norm(s: str) -> str:
    return (s or "").replace("\ufeff", "").strip()


def stable_pick(word: str, n: int) -> int:
    h = hashlib.sha256(word.encode("utf-8")).hexdigest()
    return int(h[:8], 16) % n


def natural_example(word: str) -> Tuple[str, str]:
    """
    Generates a reasonably natural, broadly compatible example pair.
    Korean line intentionally includes the English word (quoted) to avoid bad translations.
    """
    w = norm(word)
    templates: List[Tuple[str, str]] = [
        (f"Could you explain what \"{w}\" means in this sentence?", f"이 문장에서 \"{w}\"가 무슨 뜻인지 설명해 줄 수 있어요?"),
        (f"I saw the word \"{w}\" in an email at work today.", f"오늘 업무 이메일에서 \"{w}\"라는 단어를 봤어요."),
        (f"I keep hearing \"{w}\", so I looked it up.", f"\"{w}\"를 자주 들어서 찾아봤어요."),
        (f"Let's use \"{w}\" in a real conversation.", f"\"{w}\"를 실제 대화에서 써 봅시다."),
        (f"Please write a short sentence using \"{w}\".", f"\"{w}\"를 사용해서 짧은 문장을 하나 써 주세요."),
        (f"I was confused by \"{w}\" at first, but now it makes sense.", f"처음엔 \"{w}\"가 헷갈렸지만 이제 이해가 돼요."),
        (f"\"{w}\" is a useful word to remember for business English.", f"\"{w}\"는 비즈니스 영어에서 기억해 두면 유용한 단어예요."),
        (f"Can you give me another example with \"{w}\"?", f"\"{w}\"로 예문을 하나 더 들어 줄 수 있나요?"),
        (f"I wrote \"{w}\" in my notes to review later.", f"나중에 복습하려고 노트에 \"{w}\"를 적어 뒀어요."),
        (f"In this context, \"{w}\" sounds more formal.", f"이 맥락에서 \"{w}\"는 더 격식 있게 들려요."),
    ]
    idx = stable_pick(w, len(templates))
    return templates[idx]


def is_default_example(ex_eng: str, ex_kor: str, word: str) -> bool:
    w = norm(word)
    return norm(ex_eng) == f"I am studying the word {w}." and norm(ex_kor) == f"나는 {w} 단어를 공부하고 있다."


def main() -> None:
    text = DATA2.read_text(encoding="utf-8").replace("\r", "")
    lines = [ln for ln in text.split("\n") if ln.strip() != ""]

    out: List[str] = []
    replaced = 0

    i = 0
    while i < len(lines):
        m = DAY_WORD_RE.match(lines[i])
        if not m:
            # Keep as-is (shouldn't happen in normalized file, but be safe)
            out.append(lines[i] + "\n")
            i += 1
            continue

        day = m.group(1)
        word = m.group(2)
        meaning = m.group(3)
        out.append(f"{day}\t{word}\t{meaning}\n")

        if i + 1 >= len(lines):
            # missing example line; add one
            ex_eng, ex_kor = natural_example(word)
            out.append(f"\t{ex_eng}\t{ex_kor}\n")
            replaced += 1
            break

        ex_parts = lines[i + 1].split("\t")
        ex_eng = norm(ex_parts[1]) if len(ex_parts) >= 2 else ""
        ex_kor = norm(ex_parts[2]) if len(ex_parts) >= 3 else ""

        if is_default_example(ex_eng, ex_kor, word):
            new_eng, new_kor = natural_example(word)
            out.append(f"\t{new_eng}\t{new_kor}\n")
            replaced += 1
        else:
            # preserve existing examples
            out.append(lines[i + 1] + "\n")

        i += 2

    DATA2.write_text("".join(out), encoding="utf-8")
    print(f"Replaced default examples: {replaced}")


if __name__ == "__main__":
    main()

