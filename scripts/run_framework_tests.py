from __future__ import annotations

import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def run_expected_failure(command: list[str], cwd: Path, label: str) -> None:
    result = subprocess.run(command, cwd=cwd, capture_output=True, text=True, check=False)
    if result.returncode == 0:
        raise RuntimeError(f"Expected failure did not fail: {label}")
    print(f"EXPECTED FAILURE: {label}")


# Classical ML lab: prove the deliberately leaked feature produces an implausibly perfect score.
leakage = ROOT / "labs/leakage_lab"
subprocess.run([sys.executable, "make_dataset.py"], cwd=leakage, check=True)
try:
    result = subprocess.run(
        [sys.executable, "broken_pipeline.py"],
        cwd=leakage,
        capture_output=True,
        text=True,
        check=True,
    )
    score = float(result.stdout.strip().splitlines()[-1])
    if score < 0.99:
        raise RuntimeError(f"Leakage lab no longer demonstrates suspicious performance: {score}")
    print(f"LEAKAGE INJECTION: PASS ({score:.3f})")
finally:
    generated = leakage / "dataset.csv"
    if generated.exists():
        generated.unlink()

# PyTorch boss fight: the evaluator must reject the known-broken training project.
pytorch = ROOT / "labs/pytorch_boss_fight"
run_expected_failure(
    [sys.executable, "evaluator.py", "broken_train.py"],
    pytorch,
    "broken PyTorch training project",
)

# Transformer contract: the unimplemented starter must not satisfy the behavior contract.
transformer = ROOT / "labs/tiny_transformer"
run_expected_failure(
    [sys.executable, "-m", "unittest", "-v", "test_contract.py"],
    transformer,
    "unimplemented tiny-transformer starter",
)

print("FRAMEWORK LAB TESTS: PASS")
