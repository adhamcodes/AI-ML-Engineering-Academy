from __future__ import annotations

import re
import sys
from pathlib import Path
from urllib.parse import unquote

ROOT = Path(__file__).resolve().parents[1]
PHASES = [
    "00-orientation", "01-mathematical-foundations", "02-scientific-python-data",
    "03-classical-machine-learning", "04-deep-learning-pytorch", "05-vision-nlp-foundations",
    "06-transformers-llm-foundations", "07-applied-llm-engineering", "08-agents-ai-systems",
    "09-mlops-production-ai", "10-ai-system-design", "11-career-engineering",
]
LABS = [
    "diagnostic", "math_foundations", "data_quality", "leakage_lab", "pytorch_boss_fight",
    "representation_lab", "tiny_transformer", "rag_eval", "agent_eval", "mlops_service",
    "system_design_case", "evidence_audit",
]
LINK = re.compile(r"(?<!!)\[[^\]]*\]\(([^)]+)\)")


def main() -> int:
    errors: list[str] = []
    for required in ("README.md", "START-HERE.md", "ROADMAP.md", "SELF_STUDY_SYSTEM.md", "LAB_MAP.md"):
        if not (ROOT / required).is_file():
            errors.append(f"missing required file: {required}")
    for phase in PHASES:
        folder = ROOT / phase
        for name in ("README.md", "RESOURCES.md", "ASSESSMENT.md"):
            if not (folder / name).is_file():
                errors.append(f"missing phase file: {phase}/{name}")
    for lab in LABS:
        if not (ROOT / "labs" / lab / "README.md").is_file():
            errors.append(f"missing lab README: labs/{lab}/README.md")

    for md in ROOT.rglob("*.md"):
        text = md.read_text(encoding="utf-8")
        for match in LINK.finditer(text):
            raw = match.group(1).strip()
            if not raw or raw.startswith(("http://", "https://", "mailto:", "#")):
                continue
            target = unquote(raw.split(maxsplit=1)[0].strip("<>")).split("#", 1)[0]
            if not target:
                continue
            resolved = (md.parent / target).resolve()
            try:
                resolved.relative_to(ROOT)
            except ValueError:
                errors.append(f"link escapes repo: {md.relative_to(ROOT)} -> {raw}")
                continue
            if not resolved.exists():
                errors.append(f"broken local link: {md.relative_to(ROOT)} -> {raw}")

    if errors:
        print("ACADEMY QUALITY: FAIL")
        for error in errors:
            print(" -", error)
        return 1
    print("ACADEMY QUALITY: PASS")
    return 0


if __name__ == "__main__":
    sys.exit(main())
