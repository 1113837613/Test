import math


def frac(x):
    """
    返回 x 的小数部分（fractional part）。

    frac(x) = x - floor(x)

    Returns the fractional part of x.

    Examples:
        >>> frac(5.0)
        0.0
        >>> frac(0.5)
        0.5
        >>> abs(frac(3.7) - 0.7) < 1e-9
        True
        >>> abs(frac(-1.3) - 0.7) < 1e-9
        True
    """
    return x - math.floor(x)


if __name__ == "__main__":
    test_cases = [3.7, 5.0, -1.3, 0.5, 100.99, -0.1]
    for x in test_cases:
        print(f"frac({x}) = {frac(x):.10g}")
