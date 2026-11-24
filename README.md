# Gradebook – SonarQube Cloud assignment project

A small command-line student grade tracker written in Python. It reads a CSV of
student scores and prints each student's average, highest and lowest score,
letter grade, and the top student.

- **Language:** Python 3.12
- **Test framework:** pytest, with coverage from pytest-cov (`coverage.xml`)
- **CI:** GitHub Actions (`.github/workflows/sonarcloud.yml`) → SonarQube Cloud

## Run locally

```bash
pip install -r requirements-dev.txt
pytest --cov=gradebook --cov-report=xml:coverage.xml --cov-report=term
python -m gradebook.cli data/sample.csv
```
