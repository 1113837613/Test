import math
import pytest
from frac import frac


def test_positive_integer():
    assert frac(5.0) == 0.0


def test_half():
    assert frac(0.5) == 0.5


def test_positive_decimal():
    assert math.isclose(frac(3.7), 0.7)


def test_negative_decimal():
    # frac(-1.3) = -1.3 - floor(-1.3) = -1.3 - (-2) = 0.7
    assert math.isclose(frac(-1.3), 0.7)


def test_negative_small():
    # frac(-0.1) = -0.1 - (-1) = 0.9
    assert math.isclose(frac(-0.1), 0.9)


def test_zero():
    assert frac(0.0) == 0.0


def test_large_decimal():
    assert math.isclose(frac(100.99), 0.99)
