from __future__ import annotations

import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
TESTS = [
    ROOT / "labs/math_foundations/test_vector_projection.py",
    ROOT / "labs/leakage_lab/test_make_dataset.py",
    ROOT / "labs/rag_eval/evaluator.py",
    ROOT / "labs/mlops_service/test_service.py",
]
COMPILE_ONLY = [
    ROOT / "labs/leakage_lab/broken_pipeline.py",
    ROOT / "labs/pytorch_boss_fight/broken_train.py",
    ROOT / "labs/pytorch_boss_fight/evaluator.py",
    ROOT / "labs/tiny_transformer/starter.py",
    ROOT / "labs/tiny_transformer/test_contract.py",
    ROOT / "labs/agent_eval/broken_agent.py",
    ROOT / "labs/agent_eval/evaluator.py",
    ROOT / "labs/mlops_service/service.py",
]

for test in TESTS:
    subprocess.run([sys.executable, test.name], cwd=test.parent, check=True)
for source in COMPILE_ONLY:
    subprocess.run([sys.executable, "-m", "py_compile", str(source)], check=True)
print("LAB SMOKE TESTS: PASS")
