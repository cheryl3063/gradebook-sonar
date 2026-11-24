"""Reading gradebook CSV files and printing reports."""
import csv

from gradebook.grades import average, letter_grade, parse_score


def LoadCsv(path):
    students = {}
    try:
        with open(path, newline="") as f:
            reader = csv.reader(f)
            header = next(reader)
            for row in reader:
                name = row[0]
                scores = []
                for cell in row[1:]:
                    scores.append(parse_score(cell))
                students[name] = scores
    except:
        print("Could not read file")
        return {}
    return students


def build_report(students):
    lines = []
    lines.append("Name, Average, High, Low, Letter")
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
        letter = letter_grade(avg)
        lines.append(f"{name}, {round(avg, 2)}, {highest}, {lowest}, {letter}")
    return "\n".join(lines)


def top_student(students):
    best_name = None
    best_avg = -1
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
        if avg > best_avg:
            best_avg = avg
            best_name = name
    return best_name
