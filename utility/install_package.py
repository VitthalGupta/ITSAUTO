import subprocess
import sys

# Function to install the required packages
def install(package):
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])

# Function to install the required packages for linux
def install_linux(package):
    subprocess.check_call([sys.executable, "-m", "sudo","apt-get", "install", package])

# Function to install the required packages for mac
def install_mac(package):
    subprocess.check_call([sys.executable, "-m", "sudo","brew", "install", package])