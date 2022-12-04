import subprocess

# Checking for internet connection on mac
def check_internet_mac():
    try:
        subprocess.check_output(["ping", "1.1.1.1", "-c", "1"])
        return True
    except subprocess.CalledProcessError:
        return False
# Cheking connection on windows
def check_internet_win():
    try:
        subprocess.check_output(["ping", "1.1.1.1", "-n", "1"])
        return True
    except subprocess.CalledProcessError:
        return False
# Checking connection on linux
def check_internet_linux():
    try:
        subprocess.check_output(["ping", "1.1.1.1", "-c", "1"])
        return True
    except subprocess.CalledProcessError:
        return False
def check_internet(os_name):
    if os_name == "Windows":
        return check_internet_win()
    if os_name == "Linux":
        return check_internet_linux()
    if os_name == "Darwin":
        return check_internet_mac()