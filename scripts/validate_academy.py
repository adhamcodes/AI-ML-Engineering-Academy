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
# Match actionable placeholder lines, not prose that merely mentions words such as TODO.
PLACEHOLDER = re.compile(r"(?im)^\s*(?:[-*]\s*)?(?:TODO|TBD|FIXME)\s*(?::|-|$)")
SECRET_PATTERNS = [
    ("private key", re.compile(r"-----BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY-----")),
    ("GitHub token", re.compile(r"\bgh[pousr]_[A-Za-z0-9]{20,}\b")),
    ("AWS access key", re.compile(r"\bAKIA[0-9A-Z]{16}\b")),
    ("API-secret-like token", re.compile(r"\bsk-[A-Za-z0-9_-]{20,}\b")),
]
TEXT_SUFFIXES = {".md", ".py", ".json", ".yml", ".yaml", ".txt", ".sql", ".html", ".js", ".csv"}


def validate_hygiene(errors: list[str]) -> None:
    for path in sorted(ROOT.rglob("*")):
        if not path.is_file() or ".git" in path.relative_to(ROOT).parts:
            continue
        relative = path.relative_to(ROOT)
        if path.stat().st_size == 0:
            errors.append(f"unexpected empty file: {relative}")
            continue
        if path.suffix.lower() not in TEXT_SUFFIXES:
            continue
        text = path.read_text(encoding="utf-8")
        if path.suffix.lower() == ".md":
            match = PLACEHOLDER.search(text)
            if match:
                errors.append(f"actionable placeholder in {relative}: {match.group(0).strip()!r}")
        for label, pattern in SECRET_PATTERNS:
            if pattern.search(text):
                errors.append(f"possible {label} committed in {relative}")


def main() -> int:
    errors: list[str] = []
    for required in (
        "README.md", "START-HERE.md", "ROADMAP.md", "SELF_STUDY_SYSTEM.md",
        "PARALLEL_STUDY.md", "LAB_MAP.md", "requirements-labs.txt",
    ):
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

    validate_hygiene(errors)

    if errors:
        print("ACADEMY QUALITY: FAIL")
        for error in errors:
            print(" -", error)
        return 1
    print("ACADEMY QUALITY: PASS")
    print("Verified phase/lab structure, local links, actionable placeholders, empty files, and secret-pattern hygiene.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
