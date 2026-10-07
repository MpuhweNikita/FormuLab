from formulab import (
    add,
    subtract,
    multiply,
    divide,
    square_root,
    circle_area,
    triangle_area,
)


def test_add():
    assert add(10, 5) == 15


def test_subtract():
    assert subtract(10, 5) == 5


def test_multiply():
    assert multiply(10, 5) == 50


def test_divide():
    assert divide(10, 5) == 2


def test_square_root():
    assert square_root(25) == 5


def test_circle_area():
    assert circle_area(1) == 3.141592653589793


def test_triangle_area():
    assert triangle_area(10, 4) == 20