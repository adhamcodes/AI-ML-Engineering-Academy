import math
import unittest

import torch

from starter import SingleHeadSelfAttention, causal_mask, scaled_dot_product_attention


class TransformerContractTests(unittest.TestCase):
    def test_causal_mask_exactly_blocks_future_positions(self) -> None:
        mask = causal_mask(4)
        expected = torch.triu(torch.ones(4, 4, dtype=torch.bool), diagonal=1)
        self.assertEqual(tuple(mask.shape), (4, 4))
        self.assertEqual(mask.dtype, torch.bool)
        self.assertTrue(torch.equal(mask.cpu(), expected))

    def test_scaled_attention_matches_manual_reference(self) -> None:
        q = torch.tensor([[[1.0, 0.0], [0.0, 1.0]]])
        k = q.clone()
        v = torch.tensor([[[10.0, 0.0], [0.0, 20.0]]])
        scores = (q @ k.transpose(-2, -1)) / math.sqrt(2)
        expected = torch.softmax(scores, dim=-1) @ v
        actual = scaled_dot_product_attention(q, k, v)
        torch.testing.assert_close(actual, expected)

    def test_causal_mask_changes_attention_not_only_shape(self) -> None:
        q = torch.zeros(1, 2, 1)
        k = torch.zeros(1, 2, 1)
        v = torch.tensor([[[1.0], [3.0]]])
        actual = scaled_dot_product_attention(q, k, v, causal_mask(2))
        expected = torch.tensor([[[1.0], [2.0]]])
        torch.testing.assert_close(actual, expected)

    def test_module_uses_causal_self_attention(self) -> None:
        module = SingleHeadSelfAttention(2)
        identity = torch.eye(2)
        with torch.no_grad():
            module.q.weight.copy_(identity)
            module.k.weight.copy_(identity)
            module.v.weight.copy_(identity)
        x = torch.tensor([[[1.0, 0.0], [0.0, 1.0]]])
        expected = scaled_dot_product_attention(x, x, x, causal_mask(2))
        actual = module(x)
        self.assertEqual(tuple(actual.shape), tuple(x.shape))
        torch.testing.assert_close(actual, expected)


if __name__ == "__main__":
    unittest.main()
