from __future__ import annotations

import math
import torch
from torch import nn


def causal_mask(length: int, device: torch.device | None = None) -> torch.Tensor:
    raise NotImplementedError("implement a mask that blocks attention to future positions")


def scaled_dot_product_attention(q: torch.Tensor, k: torch.Tensor, v: torch.Tensor, mask: torch.Tensor | None = None) -> torch.Tensor:
    raise NotImplementedError("implement scaled attention over the sequence dimension")


class SingleHeadSelfAttention(nn.Module):
    def __init__(self, d_model: int) -> None:
        super().__init__()
        self.q = nn.Linear(d_model, d_model, bias=False)
        self.k = nn.Linear(d_model, d_model, bias=False)
        self.v = nn.Linear(d_model, d_model, bias=False)

    def forward(self, x: torch.Tensor) -> torch.Tensor:
        raise NotImplementedError("project q/k/v, apply causal attention, return contextualized values")
