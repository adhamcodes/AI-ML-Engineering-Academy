from __future__ import annotations

import json
import re
from pathlib import Path

ROOT = Path(__file__).parent


def tokens(text: str) -> set[str]:
    return set(re.findall(r"[a-z0-9]+", text.lower()))


def retrieve(question: str) -> str:
    q = tokens(question)
    best_name = ""
    best_score = -1
    for path in (ROOT / "corpus").glob("*.txt"):
        score = len(q & tokens(path.read_text(encoding="utf-8")))
        if score > best_score:
            best_name, best_score = path.name, score
    return best_name


def evaluate() -> tuple[int, int]:
    cases = json.loads((ROOT / "questions.json").read_text(encoding="utf-8"))
    correct = sum(retrieve(case["question"]) == case["expected_doc"] for case in cases)
    return correct, len(cases)


if __name__ == "__main__":
    correct, total = evaluate()
    print(f"retrieval hit@1: {correct}/{total}")
    raise SystemExit(0 if correct == total else 1)
