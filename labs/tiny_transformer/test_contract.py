import unittest

import torch

from starter import SingleHeadSelfAttention, causal_mask, scaled_dot_product_attention


class TransformerContractTests(unittest.TestCase):
    def test_causal_mask_shape_and_future_block(self) -> None:
        mask = causal_mask(4)
        self.assertEqual(tuple(mask.shape), (4, 4))
        self.assertTrue(bool(mask[0, 1]))
        self.assertFalse(bool(mask[2, 1]))

    def test_attention_shape(self) -> None:
        q = torch.randn(2, 4, 8)
        out = scaled_dot_product_attention(q, q, q, causal_mask(4))
        self.assertEqual(tuple(out.shape), (2, 4, 8))

    def test_module_shape(self) -> None:
        module = SingleHeadSelfAttention(8)
        x = torch.randn(2, 4, 8)
        self.assertEqual(tuple(module(x).shape), tuple(x.shape))


if __name__ == "__main__":
    unittest.main()
