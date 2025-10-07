import subprocess
import sys

# Needed libraries
required_libraries = ['pytest', 'webdriver_manager', 'selenium']

# Check whether libraries are installed or not
for library in required_libraries:
    try:
        __import__(library)
        print(f"{library} already installed.")
    except ImportError:
        print(f"{library} not installed. Installing...")
        subprocess.check_call([sys.executable, "-m", "pip", "install", library])

print("Requirements are satisfied.")