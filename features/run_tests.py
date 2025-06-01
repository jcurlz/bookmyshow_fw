import sys
import os
import subprocess

# Add project root to Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
def run_behave_tests_with_allure():
    behave_command = [
        "behave",
        "--tags=tag1",
        "--no-skipped",
        "-f", "allure_behave.formatter:AllureFormatter",
        "-o", "allure-results"
    ]

    try:
        print("▶ Running Behave tests with Allure formatter...")
        subprocess.run(behave_command, check=True)
        ALLURE_CMD = r"C:\Automation\Python software\allure-2.34.0\bin\allure.bat"
        print("▶ Generating Allure HTML report...")
        subprocess.run([
            "ALLURE_CMD", "generate", "allure-results", "-o", "allure-report", "--clean"
        ], check=True)

        print("✅ Allure report generated at: allure-report/index.html")

        print("▶ Opening report in browser...")
        subprocess.run(["ALLURE_CMD", "open", "allure-report"], check=True)

    except subprocess.CalledProcessError as e:
        print("❌ Failed to run tests or generate Allure report.")
        print(f"Error: {e}")

if __name__ == "__main__":
    run_behave_tests_with_allure()
