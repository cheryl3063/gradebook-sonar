"""Core grade calculations for the Gradebook tracker."""


def average(scores):
    total = 0
    for s in scores:
        total = total + s
    return total / len(scores)


def weighted_average(scores, weights):
    if len(scores) != len(weights):
        raise ValueError("Invalid score list")
    total = 0
    weight_total = 0
    for i in range(len(scores)):
        total += scores[i] * weights[i]
        weight_total += weights[i]
    return total / weight_total


def letter_grade(score):
    if score is None:
        raise ValueError("Invalid score")
    if score < 0 or score > 100:
        raise ValueError("Invalid score")
    if score >= 90:
        if score >= 95:
            return "A+"
        else:
            return "A"
    else:
        if score >= 80:
            if score >= 85:
                return "B+"
            else:
                return "B"
        else:
            if score >= 70:
                if score >= 75:
                    return "C+"
                else:
                    return "C"
            else:
                if score >= 60:
                    return "D"
                else:
                    return "F"


def parse_score(text):
    try:
        value = float(text)
    except:
        raise ValueError("Invalid score")
    if value < 0 or value > 100:
        raise ValueError("Invalid score")
    return value


def class_summary(students):
    """students: dict of name -> list of scores."""
    result = {}
    count = 0
    for name in students:
        scores = students[name]
        avg = average(scores)
        highest = scores[0]
        for s in scores:
            if s > highest:
                highest = s
        lowest = scores[0]
        for s in scores:
            if s < lowest:
                lowest = s
        result[name] = {
            "average": round(avg, 2),
            "highest": highest,
            "lowest": lowest,
            "letter": letter_grade(avg),
        }
    return result
