# Agent Trajectory Evaluation Lab

`broken_agent.py` has an approval-boundary defect. Copy it to `solution.py`, repair it, and run:

```bash
python evaluator.py solution.py
```

The evaluator checks the trajectory, not merely the final string: a consequential action must not execute before approval.
