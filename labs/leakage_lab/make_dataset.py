from __future__ import annotations

import csv
import random
from pathlib import Path

random.seed(7)
rows = []
for i in range(300):
    age = random.randint(18, 75)
    usage = random.randint(0, 100)
    noise = random.randint(-15, 15)
    target = int(usage + noise > 55)
    rows.append({"age": age, "usage": usage, "future_outcome": target, "target": target})

path = Path(__file__).with_name("dataset.csv")
with path.open("w", newline="", encoding="utf-8") as handle:
    writer = csv.DictWriter(handle, fieldnames=rows[0].keys())
    writer.writeheader()
    writer.writerows(rows)
print(path)
