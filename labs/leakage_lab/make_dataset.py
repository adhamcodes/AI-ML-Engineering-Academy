from __future__ import annotations

import csv
import random
import sys
from pathlib import Path


def generate_rows(count: int = 300, seed: int = 7) -> list[dict[str, int]]:
    rng = random.Random(seed)
    rows: list[dict[str, int]] = []
    for _ in range(count):
        age = rng.randint(18, 75)
        usage = rng.randint(0, 100)
        noise = rng.randint(-15, 15)
        target = int(usage + noise > 55)
        rows.append({"age": age, "usage": usage, "future_outcome": target, "target": target})
    return rows


def write_dataset(path: Path, count: int = 300, seed: int = 7) -> Path:
    rows = generate_rows(count=count, seed=seed)
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=rows[0].keys())
        writer.writeheader()
        writer.writerows(rows)
    return path


def main() -> None:
    path = Path(sys.argv[1]) if len(sys.argv) > 1 else Path(__file__).with_name("dataset.csv")
    print(write_dataset(path))


if __name__ == "__main__":
    main()
