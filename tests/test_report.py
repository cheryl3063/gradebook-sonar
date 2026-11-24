import pytest

from gradebook.cli import main
from gradebook.report import (
    REPORT_HEADER,
    GradebookFileError,
    build_report,
    load_csv,
    top_student,
)


def write_csv(tmp_path, text):
    path = tmp_path / "grades.csv"
    path.write_text(text, encoding="utf-8")
    return path


def test_build_report_has_header_and_row():
    lines = build_report({"Ana": [90, 80]}).splitlines()
    assert lines[0] == REPORT_HEADER
    assert lines[1] == "Ana, 85.0, 90, 80, B+"


def test_load_csv_reads_students(tmp_path):
    path = write_csv(tmp_path, "name,a1,a2\nAna,90,80\n\nBen,70,60\n")
    assert load_csv(path) == {"Ana": [90.0, 80.0], "Ben": [70.0, 60.0]}


def test_load_csv_reports_bad_score_instead_of_hiding_it(tmp_path):
    path = write_csv(tmp_path, "name,a1\nAna,ninety\n")
    with pytest.raises(GradebookFileError, match="line 2"):
        load_csv(path)


def test_load_csv_missing_file(tmp_path):
    with pytest.raises(GradebookFileError, match="Could not read"):
        load_csv(tmp_path / "missing.csv")


def test_top_student():
    assert top_student({"Ana": [90], "Ben": [95]}) == "Ben"
    assert top_student({}) is None


def test_cli_success(tmp_path, capsys):
    path = write_csv(tmp_path, "name,a1\nAna,90\n")
    assert main([str(path)]) == 0
    assert "Top student: Ana" in capsys.readouterr().out


def test_cli_usage(capsys):
    assert main([]) == 1
    assert "Usage" in capsys.readouterr().out


def test_cli_bad_file(tmp_path):
    assert main([str(tmp_path / "missing.csv")]) == 1


def test_cli_empty_file(tmp_path):
    assert main([str(write_csv(tmp_path, "name,a1\n"))]) == 1


def test_load_csv_student_with_no_scores_is_rejected_by_report(tmp_path):
    students = load_csv(write_csv(tmp_path, "name,a1\nAna\n"))
    with pytest.raises(ValueError, match="empty"):
        build_report(students)
