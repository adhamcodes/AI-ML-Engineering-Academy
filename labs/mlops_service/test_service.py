import unittest

from service import MODEL_VERSION, predict


class ServiceTests(unittest.TestCase):
    def test_prediction_contract(self) -> None:
        self.assertEqual(predict(3.0), 7.0)
        self.assertTrue(MODEL_VERSION)


if __name__ == "__main__":
    unittest.main()
