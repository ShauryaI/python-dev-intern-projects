import subprocess
import os

def get_flake8_analysis(file_path):
    try:
        # Run flake8 as a subprocess
        # capture_output=True: Capture stdout and stderr
        # text=True: Decode output as text (string) instead of bytes
        # check=True: Raise CalledProcessError if flake8 returns non-zero exit code
        result = subprocess.run(
            ["flake8", file_path],
            capture_output=True,
            text=True,
            check=True
        )
        return result.stdout  # Returns the captured output as a string
    except subprocess.CalledProcessError as e:
        # If flake8 finds issues, it returns a non-zero exit code,
        # which raises a CalledProcessError when check=True.
        # The output (errors/warnings) will be in e.stdout
        return e.stdout
    except FileNotFoundError:
        return "Error: flake8 command not found. Make sure it's installed and in your system's PATH."

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
analysis_output = get_flake8_analysis(file_name)
print("Flake8 Analysis Output:")
print(analysis_output)

# Clean up the temporary file
os.remove(file_name)
