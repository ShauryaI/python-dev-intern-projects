import subprocess
import os

def get_radon_analysis(file_path):
    try:
        # Run Radon to calculate complexity (e.g., cyclomatic complexity)
        # -s: shows the average complexity, -na: prints results from A to F
        result = subprocess.run(
            ["radon", "cc", "-s", "-na", file_path],
            capture_output=True,
            text=True,
            check=True
        )
        return result.stdout
    except subprocess.CalledProcessError as e:
        return f"Error running Radon: {e.stderr}\n"
    except FileNotFoundError:
        return "Error: radon command not found. Ensure it's installed.\n"

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
analysis_output = get_radon_analysis(file_name)
print("Radon Analysis Output:")
print(analysis_output)

# Clean up the temporary file
os.remove(file_name)
