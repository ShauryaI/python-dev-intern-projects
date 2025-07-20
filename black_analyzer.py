import subprocess

def perform_black_analysis(file_path):
    try:
        subprocess.run(
            ["black", file_path],
            capture_output=True,
            text=True,
            check=True # raise an error for black errors
        )
        return "Code formatted with Black.\n"
    except subprocess.CalledProcessError as e:
        # If flake8 finds issues, it returns a non-zero exit code,
        # which raises a CalledProcessError when check=True.
        # The output (errors/warnings) will be in e.stdout
        return e.stdout
    except FileNotFoundError:
        return "Error: black command not found. Make sure it's installed and in your system's PATH."

# Example usage:
code_to_analyze = """
def my_function():
    x=1
    y=2
    return x+y

def another_function():
    pass
"""

# Save the code to a temporary file
file_name = "temp_code.py"
with open(file_name, "w") as f:
    f.write(code_to_analyze)

# Get the flake8 analysis
analysis_output = perform_black_analysis(file_name)
print("Black Analysis Output:")
print(analysis_output)
