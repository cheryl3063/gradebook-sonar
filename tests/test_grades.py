import pytest

from gradebook.grades import (
    average,
    class_summary,
    letter_grade,
    parse_score,
    student_stats,
    weighted_average,
)


def test_average_basic():
    assert average([80, 90, 100]) == 90


@pytest.mark.parametrize(
    "score, expected",
    [
        (100, "A+"), (95, "A+"), (94.9, "A"), (90, "A"),
        (89, "B+"), (85, "B+"), (84, "B"), (80, "B"),
        (79, "C+"), (75, "C+"), (74, "C"), (70, "C"),
        (69, "D"), (60, "D"), (59.9, "F"), (0, "F"),
    ],
)
def test_letter_grade_boundaries(score, expected):
    assert letter_grade(score) == expected


@pytest.mark.parametrize("score", [None, -1, 100.1])
def test_letter_grade_rejects_invalid(score):
    with pytest.raises(ValueError):
        letter_grade(score)


def test_parse_score_valid():
    assert parse_score("88.5") == 88.5


@pytest.mark.parametrize("text", ["120", "-5", "abc", None])
def test_parse_score_invalid(text):
    with pytest.raises(ValueError):
        parse_score(text)


def test_weighted_average():
    assert weighted_average([80, 100], [1, 3]) == 95


def test_weighted_average_length_mismatch():
    with pytest.raises(ValueError):
        weighted_average([80, 90], [1])


def test_student_stats():
    assert student_stats([90, 80]) == {
        "average": 85.0, "highest": 90, "lowest": 80, "letter": "B+",
    }


def test_class_summary():
    summary = class_summary({"Ana": [90, 100], "Ben": [50, 60]})
    assert summary["Ana"]["letter"] == "A+"
    assert summary["Ben"]["letter"] == "F"


def test_average_empty_list_raises_clear_error():
    # Independently tested risk: baseline crashed with ZeroDivisionError
    with pytest.raises(ValueError, match="empty"):
        average([])


def test_weighted_average_zero_weights():
    with pytest.raises(ValueError, match="Weights"):
        weighted_average([80, 90], [0, 0])
