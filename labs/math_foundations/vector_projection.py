from __future__ import annotations


def dot(a: list[float], b: list[float]) -> float:
    if len(a) != len(b):
        raise ValueError("vectors must have equal length")
    return sum(x * y for x, y in zip(a, b))


def projection(a: list[float], onto: list[float]) -> list[float]:
    denominator = dot(onto, onto)
    if denominator == 0:
        raise ValueError("cannot project onto the zero vector")
    scale = dot(a, onto) / denominator
    return [scale * value for value in onto]
