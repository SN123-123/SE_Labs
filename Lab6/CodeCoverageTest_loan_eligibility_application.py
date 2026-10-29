
import pytest
from loan_eligibility import credit_band, is_eligible, interest_rate


@pytest.mark.parametrize("score, expected", [
    (750, "excellent"),
    (900, "excellent"),
    (749, "good"),
    (650, "good"),
    (649, "fair"),
    (550, "fair"),
    (549, "poor"),
])
def test_credit_band_valid_scores(score, expected):
    assert credit_band(score) == expected


@pytest.mark.parametrize("score", [299, 901])
def test_credit_band_invalid_scores(score):
    with pytest.raises(ValueError, match="invalid score"):
        credit_band(score)


@pytest.mark.parametrize("age, income, employment, score, expected", [
    (30, 50000, "salaried", 800, True),
    (20, 50000, "salaried", 800, False),
    (61, 50000, "salaried", 800, False),
    (30, 24999, "salaried", 800, False),
    (30, 39999, "self_employed", 800, False),
    (30, 50000, "salaried", 549, False),
    (30, 25000, "salaried", 650, True),
    (30, 40000, "self_employed", 650, True),
])
def test_is_eligible(age, income, employment, score, expected):
    assert is_eligible(age, income, employment, score) is expected


def test_unknown_employment():
    with pytest.raises(ValueError, match="unknown employment"):
        is_eligible(30, 50000, "unemployed", 800)


@pytest.mark.parametrize("score, employment, collateral, expected", [
    (800, "salaried", False, 8),
    (700, "salaried", False, 10),
    (600, "salaried", False, 13),
    (800, "self_employed", False, 9),
    (700, "self_employed", True, 9),
    (600, "salaried", True, 11),
])
def test_interest_rate(score, employment, collateral, expected):
    assert interest_rate(score, employment, collateral) == expected
