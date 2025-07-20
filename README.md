# python-dev-intern-projects
Python Developer Internship Projects

This branch is for AI Code Reviewer

## Creating a web application using Gradio ##
1. File name gradio_web.py
2. pip install gradio
3. python gradio_web.py
* Running on local URL:  http://127.0.0.1:7860
* To create a public link, set `share=True` in `launch()`.
Use as API is a very good feature
* gradio gradio_web.py -- to rerun on file change
* gradio ai_code_reviewer.py --encoding cp1252 -- loading error popup is visible. Does not fade away quickly.
* hot reload issue

## NiceGUI ##
>>> pip install nicegui
Hot reload is active by default
NiceGUI ready to go on http://localhost:8080, http://169.254.187.125:8080, http://169.254.245.183:8080, http://169.254.53.110:8080, and http://192.168.225.137:8080

Integrating Flake8, Black, and Radon for a comprehensive review

    Flake8: Ensures adherence to PEP 8, catches syntax errors, and identifies potential bugs like unused variables.
    Black: Standardizes code formatting, making it consistent and readable.
    Radon: Calculates code complexity metrics (like Cyclomatic Complexity, Maintainability Index), helping identify areas that might be hard to understand or maintain.

Using Flake8 for code quality and style checks

Flake8 checks Python code against PEP 8 style guidelines, finds syntax errors, and identifies potential bugs. It integrates pyflakes for program error checking, pycodestyle for PEP 8 compliance, and McCabe for complexity checks.

>>>pip install flake8
>>>pip install black

Formatting: Run Black on a file (black your_script.py) or a directory (black .).
black --check black_analyzer.py

>>>pip install pylint

now radon
>>>pip install radon

>>> now ai