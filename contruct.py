import sys
import os

if sys.prefix != sys.base_prefix:
    print("MATRIX STATUS: Welcome to the construct\n")
    print(f"Current Python: {sys.base_prefix}")
    print(f"Virtual Environment: {os.path.basename(sys.prefix)}")
    print(f"Environment path: {sys.prefix}\n")
    print("SUCCESS: You're in an isolated environment!")
    print("Safe to install packages without affecting the global system.\n")
    print("Package installation path:")
    print("?")
else:
    print("MATRIX STATUS: You're still plugged in\n")
    print(f"Current Python: {sys.base_prefix}")
    print("Virtual Environment: None detected")
    print("WARNING: You're in the global environment!")
    print("The machines can see everything you install.\n")
    print("To enter the construct, run:")
    print("python -m venv matrix_env")
    print("source matrix_env/bin/activate # On Unix")
    print("matrix_env\Scripts\activate # On Windows\n")
    print("Then run this program again.")
