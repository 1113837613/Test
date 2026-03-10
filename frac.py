import math


def frac(x):
    """返回实数 x 的小数部分（fractional part）。

    定义: frac(x) = x - floor(x)
    结果始终满足 0 <= frac(x) < 1。

    示例:
        >>> round(frac(3.7), 10)
        0.7
        >>> frac(-1.3)
        0.7
        >>> frac(5.0)
        0.0
    """
    return x - math.floor(x)


if __name__ == "__main__":
    examples = [3.7, -1.3, 5.0, 0.5, -2.0, 100.99]
    for x in examples:
        print(f"frac({x}) = {frac(x)}")
