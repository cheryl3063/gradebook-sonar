import pytest

from gradebook.grades import average, letter_grade, parse_score


def test_average_basic():
    assert average([80, 90, 100]) == 90


def test_letter_grade_a():
    assert letter_grade(92) == "A"


def test_letter_grade_f():
    assert letter_grade(40) == "F"


def test_parse_score_valid():
    assert parse_score("88.5") == 88.5


def test_parse_score_out_of_range():
    with pytest.raises(ValueError):
        parse_score("120")
