import os
import ast
import logging
from datetime import datetime


# -----------------------------
# Logging Configuration
# -----------------------------
logging.basicConfig(
    filename="app.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)


# -----------------------------
# Scan Python Files
# -----------------------------
def scan_python_files(folder_path):
    python_files = []

    for file in os.listdir(folder_path):
        if file == "sample.py":
            python_files.append(os.path.join(folder_path, file))

    return python_files

# -----------------------------
# Analyze Code Metrics
# -----------------------------
def analyze_metrics(tree):
    metrics = {
        "functions": 0,
        "classes": 0,
        "imports": 0
    }

    for node in ast.walk(tree):

        if isinstance(node, ast.FunctionDef):
            metrics["functions"] += 1

        elif isinstance(node, ast.ClassDef):
            metrics["classes"] += 1

        elif isinstance(node, (ast.Import, ast.ImportFrom)):
            metrics["imports"] += 1

    return metrics


# -----------------------------
# Check Missing Docstrings
# -----------------------------
def check_docstrings(tree):
    issues = []

    for node in ast.walk(tree):

        if isinstance(node, ast.FunctionDef):
            if ast.get_docstring(node) is None:
                issues.append(
                    f"Function '{node.name}' is missing a docstring."
                )

        elif isinstance(node, ast.ClassDef):
            if ast.get_docstring(node) is None:
                issues.append(
                    f"Class '{node.name}' is missing a docstring."
                )

    return issues


# -----------------------------
# Check Missing Type Hints
# -----------------------------
def check_type_hints(tree):
    issues = []

    for node in ast.walk(tree):

        if isinstance(node, ast.FunctionDef):

            missing_hint = False

            for arg in node.args.args:
                if arg.annotation is None:
                    missing_hint = True

            if node.returns is None:
                missing_hint = True

            if missing_hint:
                issues.append(
                    f"Function '{node.name}' is missing type hints."
                )

    return issues


# -----------------------------
# Quality Score
# -----------------------------
def calculate_quality_score(issue_count):
    score = max(0, 100 - (issue_count * 5))
    return score


# -----------------------------
# AI Improvement Suggestions
# -----------------------------
def generate_ai_suggestions(issues):
    suggestions = []

    for issue in issues:

        if "docstring" in issue.lower():
            suggestions.append(
                "Add meaningful docstrings describing the purpose and usage of the function/class."
            )

        if "type hints" in issue.lower():
            suggestions.append(
                "Add parameter and return type annotations for improved readability and maintainability."
            )

    return list(set(suggestions))


# -----------------------------
# Generate Test Cases
# -----------------------------
def generate_test_cases():
    tests = [
        "Test function counting.",
        "Test class counting.",
        "Test import counting.",
        "Test missing docstring detection.",
        "Test missing type hint detection."
    ]

    return tests


# -----------------------------
# Generate Report
# -----------------------------
def generate_report(
    files_scanned,
    metrics,
    issues,
    suggestions,
    tests,
    score
):
    report_name = "quality_report.txt"

    with open(report_name, "w", encoding="utf-8") as report:

        report.write("=" * 50 + "\n")
        report.write("AI-ASSISTED PYTHON CODE QUALITY REPORT\n")
        report.write("=" * 50 + "\n\n")

        report.write(
            f"Generated On: {datetime.now()}\n\n"
        )

        report.write(
            f"Files Scanned : {files_scanned}\n\n"
        )

        report.write("CODE METRICS\n")
        report.write("-" * 20 + "\n")

        report.write(
            f"Functions : {metrics['functions']}\n"
        )

        report.write(
            f"Classes   : {metrics['classes']}\n"
        )

        report.write(
            f"Imports   : {metrics['imports']}\n\n"
        )

        report.write("ISSUES FOUND\n")
        report.write("-" * 20 + "\n")

        if issues:
            for issue in issues:
                report.write(f"- {issue}\n")
        else:
            report.write("No issues found.\n")

        report.write("\n")

        report.write("QUALITY SCORE\n")
        report.write("-" * 20 + "\n")
        report.write(f"{score}/100\n\n")

        report.write("AI IMPROVEMENT SUGGESTIONS\n")
        report.write("-" * 20 + "\n")

        for suggestion in suggestions:
            report.write(f"- {suggestion}\n")

        report.write("\n")

        report.write("GENERATED TEST CASES\n")
        report.write("-" * 20 + "\n")

        for test in tests:
            report.write(f"- {test}\n")

    logging.info("Report generated successfully.")


# -----------------------------
# Main Function
# -----------------------------
def main():

    print("\n" + "=" * 50)
    print("AI-ASSISTED PYTHON CODE QUALITY ANALYZER")
    print("=" * 50)

    current_directory = os.getcwd()

    python_files = scan_python_files(current_directory)

    total_metrics = {
        "functions": 0,
        "classes": 0,
        "imports": 0
    }

    all_issues = []

    for file_path in python_files:

        try:

            with open(file_path, "r", encoding="utf-8") as file:
                source_code = file.read()

            tree = ast.parse(source_code)

            metrics = analyze_metrics(tree)

            total_metrics["functions"] += metrics["functions"]
            total_metrics["classes"] += metrics["classes"]
            total_metrics["imports"] += metrics["imports"]

            all_issues.extend(
                check_docstrings(tree)
            )

            all_issues.extend(
                check_type_hints(tree)
            )

            logging.info(
                f"Successfully analyzed {file_path}"
            )

        except Exception as e:
            logging.error(
                f"Error processing {file_path}: {e}"
            )

    score = calculate_quality_score(
        len(all_issues)
    )

    suggestions = generate_ai_suggestions(
        all_issues
    )

    test_cases = generate_test_cases()

    generate_report(
        len(python_files),
        total_metrics,
        all_issues,
        suggestions,
        test_cases,
        score
    )

    print(f"\nFiles Scanned : {len(python_files)}")
    print(
        f"Functions     : {total_metrics['functions']}"
    )
    print(
        f"Classes       : {total_metrics['classes']}"
    )
    print(
        f"Imports       : {total_metrics['imports']}"
    )
    print(f"Quality Score : {score}/100")

    print(
        "\nReport Generated Successfully!"
    )

    print(
        "Check quality_report.txt and app.log"
    )





# -----------------------------
# Program Entry Point
# -----------------------------
if __name__ == "__main__":
    main()