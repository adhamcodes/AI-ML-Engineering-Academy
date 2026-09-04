from __future__ import annotations

import importlib.util
import math
import sys
from pathlib import Path


def load(path: str):
    spec = importlib.util.spec_from_file_location("learner_training", Path(path))
    if spec is None or spec.loader is None:
        raise RuntimeError("cannot load solution")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def evaluate(path: str) -> None:
    module = load(path)
    a = module.run(seed=123)
    b = module.run(seed=123)
    for result in (a, b):
        if set(result) < {"train_loss", "valid_loss"}:
            raise AssertionError("run() must report train_loss and valid_loss")
        if not all(math.isfinite(float(value)) for value in result.values()):
            raise AssertionError("metrics must be finite")
    if abs(a["valid_loss"] - b["valid_loss"]) > 1e-8:
        raise AssertionError("same seed should reproduce validation metric")
    print("PYTORCH MINIMUM GATE: PASS")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        raise SystemExit("usage: python evaluator.py solution.py")
    evaluate(sys.argv[1])
