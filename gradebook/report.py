"""Reading gradebook CSV files and printing reports."""
import csv

from gradebook.grades import average, parse_score, student_stats

REPORT_HEADER = "Name, Average, High, Low, Letter"


class GradebookFileError(Exception):
    """Raised when a gradebook CSV file cannot be read or contains bad data."""


def load_csv(path):
    students = {}
    try:
        with open(path, newline="", encoding="utf-8") as f:
            reader = csv.reader(f)
            next(reader, None)  # skip header row
            for line_number, row in enumerate(reader, start=2):
                if not row:
                    continue
                try:
                    students[row[0]] = [parse_score(cell) for cell in row[1:]]
                except ValueError as error:
                    raise GradebookFileError(
                        f"{path}, line {line_number}: {error}"
                    ) from error
    except OSError as error:
        raise GradebookFileError(f"Could not read {path}: {error}") from error
    return students


def build_report(students):
    lines = [REPORT_HEADER]
    for name, scores in students.items():
        stats = student_stats(scores)
        lines.append(
            f"{name}, {stats['average']}, {stats['highest']}, "
            f"{stats['lowest']}, {stats['letter']}"
        )
    return "\n".join(lines)


def top_student(students):
    if not students:
        return None
    return max(students, key=lambda name: average(students[name]))
