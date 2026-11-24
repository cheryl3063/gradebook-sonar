from gradebook.report import build_report


def test_build_report_has_header_and_row():
    text = build_report({"Ana": [90, 80]})
    lines = text.splitlines()
    assert lines[0] == "Name, Average, High, Low, Letter"
    assert lines[1] == "Ana, 85.0, 90, 80, B+"
