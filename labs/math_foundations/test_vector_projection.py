import unittest

from vector_projection import dot, projection


class VectorTests(unittest.TestCase):
    def test_dot(self) -> None:
        self.assertEqual(dot([1, 2, 3], [4, 5, 6]), 32)

    def test_projection(self) -> None:
        self.assertEqual(projection([2, 2], [1, 0]), [2.0, 0.0])

    def test_zero_basis_rejected(self) -> None:
        with self.assertRaises(ValueError):
            projection([1, 2], [0, 0])


if __name__ == "__main__":
    unittest.main()
