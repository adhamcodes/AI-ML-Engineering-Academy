from __future__ import annotations

import importlib.util
import sys
from pathlib import Path


def load(path: str):
    spec = importlib.util.spec_from_file_location("agent_solution", Path(path))
    if spec is None or spec.loader is None:
        raise RuntimeError("cannot load solution")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def evaluate(path: str) -> None:
    agent = load(path).Agent()
    denied = agent.run("delete_account", approved=False)
    allowed = agent.run("delete_account", approved=True)
    assert "delete_account" not in denied, denied
    assert "request_approval" in denied, denied
    assert "delete_account" in allowed, allowed
    assert allowed.index("delete_account") > allowed.index("request_approval"), allowed
    print("AGENT TRAJECTORY: PASS")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        raise SystemExit("usage: python evaluator.py solution.py")
    evaluate(sys.argv[1])
