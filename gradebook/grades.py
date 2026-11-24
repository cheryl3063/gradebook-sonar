"""Core grade calculations for the Gradebook tracker."""

INVALID_SCORE = "Invalid score"

# (minimum score, letter) from highest to lowest; first match wins
GRADE_BANDS = (
    (95, "A+"),
    (90, "A"),
    (85, "B+"),
    (80, "B"),
    (75, "C+"),
    (70, "C"),
    (60, "D"),
)


def average(scores):
    return sum(scores) / len(scores)


def weighted_average(scores, weights):
    if len(scores) != len(weights):
        raise ValueError("Invalid score list")
    total = sum(score * weight for score, weight in zip(scores, weights))
    return total / sum(weights)


def letter_grade(score):
    if score is None or score < 0 or score > 100:
        raise ValueError(INVALID_SCORE)
    for minimum, letter in GRADE_BANDS:
        if score >= minimum:
            return letter
    return "F"


def parse_score(text):
    try:
        value = float(text)
    except (TypeError, ValueError) as error:
        raise ValueError(INVALID_SCORE) from error
    if value < 0 or value > 100:
        raise ValueError(INVALID_SCORE)
    return value


def student_stats(scores):
    """Return average, highest, lowest and letter grade for one student."""
    avg = average(scores)
    return {
        "average": round(avg, 2),
        "highest": max(scores),
        "lowest": min(scores),
        "letter": letter_grade(avg),
    }


def class_summary(students):
    """students: dict of name -> list of scores."""
    return {name: student_stats(scores) for name, scores in students.items()}
