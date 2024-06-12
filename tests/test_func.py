import pytest

from main import calculator, add, subtract, multiply, divide


@pytest.mark.parametrize(
    ("x", "y", "res"),
    [
        (10, 5, 15),
        (2.5, 1.5, 4),
        (0, 0, 0),
    ],
)
def test_add(x, y, res):
    assert add(x, y) == res


@pytest.mark.parametrize(
    ("x", "y", "res"),
    [
        (10, 5, 5),
        (3, 5, -2),
        (0, 0, 0),
    ],
)
def test_sub(x, y, res):
    assert subtract(x, y) == res


@pytest.mark.parametrize(
    ("x", "y", "res"),
    [
        (10, 5, 50),
        (0, 5, 0),
        (5, -1, -5),
    ],
)
def test_mult(x, y, res):
    assert multiply(x, y) == res


@pytest.mark.parametrize(
    ("x", "y", "res"),
    [
        (10, 5, 2),
        (0, 5, 0),
        (5, 0, -1),
    ],
)
def test_div(x, y, res):
    assert divide(x, y) == res


@pytest.mark.parametrize(
    ("x", "y", "op", "res"),
    [
        (10, 5, "+", 15),
        (10, 5, "-", 5),
        (10, 5, "*", 50),
        (10, 5, "/", 2),
    ],
)
def test_calc(x, y, op, res):
    assert calculator(x, y, op) == res
