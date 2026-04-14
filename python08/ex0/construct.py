import sys
import os
import site

if sys.prefix != sys.base_prefix:
    print("MATRIX STATUS: Welcome to the construct\n")
    print("Current Python:", sys.executable)
    print("Virtual Environment:", os.path.basename(sys.prefix))
    print("Environment path:", sys.prefix)

    print("\nSUCCESS: You're in an isolated environment!")
    print("Safe to install packages without affecting the global system.\n")

    path = site.getsitepackages()
    print("Package installation path:", path[0])
else:
    print("MATRIX STATUS: You're still plugged in\n")

    print("Current Python:", sys.executable)
    print("Virtual Environment:", os.path.basename(sys.prefix))

    print("\nWARNING: You're in the global environment!")
    print("The machines can see everything you install.\n")

    print("To enter the construct, run:")
    print("python3 -m venv matrix_env")
    print("source matrix_env/bin/activate\n")

    print("Then run this program again.")
