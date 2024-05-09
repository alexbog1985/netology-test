import pytest
from square import Square


@pytest.mark.parametrize("a, expected",
                         (
                             [5, 20],
                             [4, 16],
                             [8, 32],
                         ))
def test_square_perimeter(a, expected):
    actual = Square(a).get_perimeter()
    assert actual == expected


# @pytest.mark.xfail
@pytest.mark.parametrize("a, expected",
                         (
                             [5, 25],
                             [4, 16],
                             # [-4, "Сторона квадрата не может быть отрицательной"],
                         ))
def test_square_area(a, expected):
    actual = Square(a).get_area()
    assert actual == expected
