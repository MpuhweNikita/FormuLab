from formulab import (
    mean,
    median,
    variance,
    standard_deviation,
)


def test_mean():
    assert mean([10, 20, 30]) == 20


def test_median():
    assert median([10, 30, 20]) == 20


def test_variance():
    assert variance([1, 2, 3]) == 2 / 3


def test_standard_deviation():
    assert round(standard_deviation([1, 2, 3]), 5) == 0.81650