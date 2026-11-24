"""Command-line entry point: python -m gradebook.cli data/sample.csv"""
import sys

from gradebook.report import LoadCsv, build_report, top_student


def main(argv=None):
    argv = argv if argv is not None else sys.argv[1:]
    if not argv:
        print("Usage: python -m gradebook.cli <file.csv>")
        return 1
    students = LoadCsv(argv[0])
    if not students:
        return 1
    print(build_report(students))
    print(f"Top student: {top_student(students)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
