from __future__ import annotations

import torch
from torch import nn


def make_data() -> tuple[torch.Tensor, torch.Tensor]:
    x = torch.linspace(-2, 2, 128).unsqueeze(1)
    y = 3 * x + 0.5 + 0.2 * torch.randn_like(x)
    return x, y


def run(seed: int = 0) -> dict[str, float]:
    # Deliberate defects are present. Diagnose before changing code.
    x, y = make_data()
    x_train, y_train = x[:96], y[:96]
    x_valid, y_valid = x_train, y_train

    model = nn.Sequential(nn.Linear(1, 16), nn.ReLU(), nn.Dropout(0.4), nn.Linear(16, 1))
    optimizer = torch.optim.SGD(model.parameters(), lr=0.05)
    loss_fn = nn.MSELoss()

    model.train()
    for _ in range(80):
        prediction = model(x_train)
        loss = loss_fn(prediction, y_train)
        loss.backward()
        optimizer.step()

    with torch.no_grad():
        valid_loss = loss_fn(model(x_valid), y_valid)
    return {"train_loss": float(loss.detach()), "valid_loss": float(valid_loss)}


if __name__ == "__main__":
    print(run())
