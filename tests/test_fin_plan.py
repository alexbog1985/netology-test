import pytest
from fin_plan import FinPlan


@pytest.mark.parametrize("test_input, expected",
                         (
                             [(100000, 30, 50), 360000.0],
                         ))
def test_fin_plan_mortgage(test_input, expected):
    fp = FinPlan(*test_input)
    assert fp.mortgage == expected


@pytest.mark.parametrize("test_input, expected",
                         (
                             [(100000, 30, 50), 240000.0],
                         ))
def test_fin_plan_fin_plan(test_input, expected):
    fp = FinPlan(*test_input)
    assert fp.fin_plan == expected
