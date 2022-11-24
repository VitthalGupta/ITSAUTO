import subprocess
import sys

# Function to install the required packages
def install(package):
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])
