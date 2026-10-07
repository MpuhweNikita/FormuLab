"""
Statistical functions for FormuLab.

Provides basic descriptive statistics for numerical datasets.
"""

import math


def _validate_data(numbers: list[float]) -> None:
    """Validate that a dataset is not empty."""
    if not numbers:
        raise ValueError("The dataset cannot be empty.")


def mean(numbers: list[float]) -> float:
    """Return the arithmetic mean."""
    _validate_data(numbers)
    return sum(numbers) / len(numbers)


def median(numbers: list[float]) -> float:
    """Return the median value."""
    _validate_data(numbers)

    sorted_numbers = sorted(numbers)
    n = len(sorted_numbers)
    middle = n // 2

    if n % 2 == 0:
        return (
            sorted_numbers[middle - 1]
            + sorted_numbers[middle]
        ) / 2

    return sorted_numbers[middle]


def variance(numbers: list[float]) -> float:
    """Return the population variance."""
    _validate_data(numbers)

    average = mean(numbers)

    return sum(
        (number - average) ** 2
        for number in numbers
    ) / len(numbers)


def standard_deviation(numbers: list[float]) -> float:
    """Return the population standard deviation."""
    return math.sqrt(variance(numbers))