import pytest
from rectangle import rectangle


@pytest.mark.parametrize("a, b, expected",
                         (
                             [1, 1, 4],
                             [2, 2, 8],
                         ))
def test_rectangle_perimeter(a, b, expected):
    actual = rectangle(a, b)['Периметр']
    assert actual == expected


@pytest.mark.parametrize("a, b, expected",
                         (
                             [1, 1, 1],
                             [2, 2, 4],
                         ))
def test_rectangle_area(a, b, expected):
    actual = rectangle(a, b)['Площадь']
    assert actual == expected
