"""
Mathematical functions for FormuLab.

FormuLab provides simple, reusable mathematical calculations
for students, developers, and scientific applications.
"""

import math as _math


def add(a: float, b: float) -> float:
    """Return the sum of two numbers."""
    return a + b


def subtract(a: float, b: float) -> float:
    """Return the difference between two numbers."""
    return a - b


def multiply(a: float, b: float) -> float:
    """Return the product of two numbers."""
    return a * b


def divide(a: float, b: float) -> float:
    """Return a divided by b.

    Raises:
        ZeroDivisionError: If b is zero.
    """
    if b == 0:
        raise ZeroDivisionError("Cannot divide by zero.")
    return a / b


def power(base: float, exponent: float) -> float:
    """Return base raised to the given exponent."""
    return base ** exponent


def square_root(number: float) -> float:
    """Return the square root of a non-negative number."""
    if number < 0:
        raise ValueError("Square root requires a non-negative number.")
    return _math.sqrt(number)


def factorial(number: int) -> int:
    """Return the factorial of a non-negative integer."""
    if number < 0:
        raise ValueError("Factorial requires a non-negative integer.")

    if not isinstance(number, int):
        raise TypeError("Factorial requires an integer.")

    return _math.factorial(number)


def percentage(value: float, percent: float) -> float:
    """Return a percentage of a value."""
    return value * (percent / 100)


def quadratic_roots(a: float, b: float, c: float) -> tuple[complex, complex]:
    """Return the two roots of ax² + bx + c = 0.

    Complex roots are returned when the discriminant is negative.
    """
    if a == 0:
        raise ValueError("Coefficient 'a' cannot be zero.")

    discriminant = b**2 - 4*a*c

    if discriminant >= 0:
        root1 = (-b + _math.sqrt(discriminant)) / (2*a)
        root2 = (-b - _math.sqrt(discriminant)) / (2*a)
    else:
        imaginary_part = _math.sqrt(-discriminant) / (2*a)
        real_part = -b / (2*a)

        root1 = complex(real_part, imaginary_part)
        root2 = complex(real_part, -imaginary_part)

    return root1, root2


def circle_area(radius: float) -> float:
    """Return the area of a circle."""
    if radius < 0:
        raise ValueError("Radius cannot be negative.")
    return _math.pi * radius**2


def circle_circumference(radius: float) -> float:
    """Return the circumference of a circle."""
    if radius < 0:
        raise ValueError("Radius cannot be negative.")
    return 2 * _math.pi * radius


def rectangle_area(length: float, width: float) -> float:
    """Return the area of a rectangle."""
    if length < 0 or width < 0:
        raise ValueError("Length and width cannot be negative.")
    return length * width


def triangle_area(base: float, height: float) -> float:
    """Return the area of a triangle."""
    if base < 0 or height < 0:
        raise ValueError("Base and height cannot be negative.")
    return 0.5 * base * height