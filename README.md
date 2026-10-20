# AIPython_Code_Analyzer

#Project Overview

  The AI-Assisted Python Code Quality & Documentation Analyzer is a Python-based utility that scans Python source files and evaluates their code   quality. The tool analyzes files to identify missing docstrings, missing type hints, and other basic code-quality issues while generating actionable improvement suggestions.
  
  The project aims to help developers improve code readability, maintainability, and documentation standards through automated analysis and AI-assisted recommendations.

#Objectives
Scan Python source files.
Count functions, classes, and imports.
Detect missing docstrings.
Detect missing type hints.
Generate a code-quality report.
Provide AI-assisted improvement suggestions.
Generate test case recommendations.
Maintain execution logs.

#Features
Code Analysis
Scans Python (.py) files in the project directory.
Parses source code using Python's AST module.
Metrics Generation

#Counts:
Functions
Classes
Imports

#Quality Checks
Identifies functions without docstrings.
Identifies classes without docstrings.
Identifies functions without type hints.

#AI-Assisted Suggestions
Recommends adding meaningful docstrings.
Recommends adding parameter and return type annotations.
Provides guidance for improving code quality.

#Reporting
Generates a detailed quality report (quality_report.txt).
Calculates a quality score based on detected issues.

#Logging
Creates an execution log (app.log) to track analysis activity and errors.

#Technologies Used
Python 3.x
AST (Abstract Syntax Tree)
OS Module
Logging Module
Datetime Module
Project Structure
Plain Text

#AI_Python_Code_Analyzer/
│
├── main.py
├── __init__.py
├── teams.txt
├── sample.py
├── quality_report.txt
└── app.log


#Execution Steps
Place Python files to be analyzed in the project folder.
Open a terminal in the project directory.

#Run the application:
Shell
python main.py
View the generated report:
Plain Text
quality_report.txt

#View execution logs:
Plain Text
app.log
Sample Input
Python

import math
def add(a,b):
return a+b
 
class Student:
pass


#Sample Output
Plain Text
Files Scanned : 1
Functions : 1
Classes : 1
Imports : 1
Quality Score : 85/100
 
Generated Outputs
Quality Report

Contains:

Code metrics
Detected issues
Quality score
AI improvement suggestions
Test recommendations
Log File

Contains:

Analysis execution details
Process information
Error records (if any)
AI-Assisted Improvements

Example recommendation:

Python
def add(a: int, b: int) -> int:
"""Return the sum of two integers."""
return a + b
 

The analyzer suggests documentation and type annotations to improve code maintainability and readability.

Conclusion

This project demonstrates the use of core Python concepts such as file handling, AST-based code analysis, logging, exception handling, and automated reporting. It provides developers with a simple yet effective way to assess and improve Python code quality through AI-assisted recommendations.
