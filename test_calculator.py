import pytest

from calculator import add, divide, multiply, subtract

@pytest.mark.parametrize(
    ("a", "b", "expected"),
    [
        (2, 3, 5),
        (-2, 3, 1),
        (-2, -3, -5),
        (0, 0, 0),
        (1.5, 2.5, 4.0),
    ],
)
def test_add(a, b, expected):
    assert add(a, b) == expected


@pytest.mark.parametrize(
    ("a", "b", "expected"),
    [
        (5, 3, 2),
        (-2, 3, -5),
        (-2, -3, 1),
        (0, 0, 0),
        (5.5, 2.5, 3.0),
    ],
)
def test_subtract(a, b, expected):
    assert subtract(a, b) == expected


@pytest.mark.parametrize(
    ("a", "b", "expected"),
    [
        (2, 3, 6),
        (-2, 3, -6),
        (-2, -3, 6),
        (0, 99, 0),
        (1.5, 2, 3.0),
    ],
)
def test_multiply(a, b, expected):
    assert multiply(a, b) == expected


@pytest.mark.parametrize(
    ("a", "b", "expected"),
    [
        (6, 3, 2),
        (-6, 3, -2),
        (-6, -3, 2),
        (0, 5, 0),
        (5, 2, 2.5),
    ],
)
def test_divide(a, b, expected):
    assert divide(a, b) == expected


@pytest.mark.parametrize("a", [0, 1, -1, 3.5])
def test_divide_by_zero(a):
    with pytest.raises(ValueError, match="Cannot divide by zero"):
        divide(a, 0)
