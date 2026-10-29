
import pytest
from loan_eligibility import credit_band, is_eligible, interest_rate


@pytest.mark.parametrize(
    "score, expected",
    [
        (299, "invalid"),
        (300, "poor"),
        (549, "poor"),
        (550, "fair"),
        (649, "fair"),
        (650, "good"),
        (749, "good"),
        (750, "excellent"),
        (900, "excellent"),
        (901, "invalid"),
    ],
)
def test_credit_band_branches(score, expected):
    if expected == "invalid":
        with pytest.raises(ValueError, match="invalid score"):
            credit_band(score)
    else:
        assert credit_band(score) == expected


@pytest.mark.parametrize(
    "age, income, employment, score, expected",
    [
        (20, 50000, "salaried", 800, False),
        (21, 25000, "salaried", 650, True),
        (60, 25000, "salaried", 650, True),
        (61, 50000, "salaried", 800, False),
        (30, 24999, "salaried", 800, False),
        (30, 25000, "salaried", 800, True),
        (30, 39999, "self_employed", 800, False),
        (30, 40000, "self_employed", 800, True),
        (30, 50000, "salaried", 549, False),
        (30, 50000, "salaried", 550, True),
    ],
)
def test_eligibility_branches(age, income, employment, score, expected):
    assert is_eligible(age, income, employment, score) is expected


def test_unknown_employment_branch():
    with pytest.raises(ValueError, match="unknown employment"):
        is_eligible(30, 50000, "unemployed", 800)


@pytest.mark.parametrize(
    "score, employment, collateral, expected",
    [
        (750, "salaried", False, 8),
        (749, "salaried", False, 10),
        (650, "salaried", False, 10),
        (649, "salaried", False, 13),
        (550, "salaried", False, 13),
        (800, "self_employed", False, 9),
        (800, "salaried", True, 6),
        (800, "self_employed", True, 7),
    ],
)
def test_interest_rate_branches(score, employment, collateral, expected):
    assert interest_rate(score, employment, collateral) == expected
