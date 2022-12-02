import subprocess

# Checking for internet connection
def check_internet():
    try:
        subprocess.check_output(["ping", "1.1.1.1", "-c", "1"])
        return True
    except subprocess.CalledProcessError:
        return False

def check_internet_windows():
    try:
        subprocess.check_output(["ping", "1.1.1.1"])
        return True
    except subprocess.CalledProcessError:
        return False