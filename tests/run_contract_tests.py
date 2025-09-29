#!/usr/bin/env python3
"""
Script to run contract tests and verify they fail (TDD approach)
"""

import subprocess
import sys
import os

def run_tests():
    """Run contract tests and return results"""
    # Change to the project root directory
    os.chdir(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

    # Run contract tests only
    result = subprocess.run([
        sys.executable, "-m", "pytest",
        "tests/contract/",
        "-m", "contract",
        "-v", "--tb=short"
    ], capture_output=True, text=True)

    return result.returncode, result.stdout, result.stderr

def main():
    """Main function to check if tests fail as expected"""
    print("Running contract tests (should fail - TDD)...")
    print("=" * 50)

    return_code, stdout, stderr = run_tests()

    print("STDOUT:")
    print(stdout)

    if stderr:
        print("STDERR:")
        print(stderr)

    print("=" * 50)
    print(f"Return code: {return_code}")

    if return_code != 0:
        print("SUCCESS: Tests are failing as expected (TDD)")
        print("\nThis is correct behavior - the implementations don't exist yet.")
        print("After implementing the APIs, these tests should pass.")
        return 0
    else:
        print("UNEXPECTED: Tests are passing without implementation!")
        print("This suggests the tests might not be properly testing the APIs.")
        return 1

if __name__ == "__main__":
    sys.exit(main())