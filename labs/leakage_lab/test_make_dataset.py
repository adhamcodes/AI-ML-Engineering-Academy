from __future__ import annotations

import csv
import tempfile
import unittest
from pathlib import Path

from make_dataset import generate_rows, write_dataset


class DatasetTests(unittest.TestCase):
    def test_same_seed_reproduces_rows(self) -> None:
        self.assertEqual(generate_rows(count=20, seed=7), generate_rows(count=20, seed=7))
        self.assertNotEqual(generate_rows(count=20, seed=7), generate_rows(count=20, seed=8))

    def test_forbidden_feature_really_leaks_target(self) -> None:
        rows = generate_rows(count=50, seed=7)
        self.assertTrue(all(row["future_outcome"] == row["target"] for row in rows))

    def test_writer_produces_requested_row_count(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            path = write_dataset(Path(temp) / "dataset.csv", count=25, seed=7)
            with path.open(newline="", encoding="utf-8") as handle:
                rows = list(csv.DictReader(handle))
            self.assertEqual(len(rows), 25)
            self.assertEqual(set(rows[0]), {"age", "usage", "future_outcome", "target"})


if __name__ == "__main__":
    unittest.main()
