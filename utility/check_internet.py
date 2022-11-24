import subprocess

# Checking for internet connection
def check_internet():
    try:
        subprocess.check_output(["ping", "www.google.com", "-c", "3"])
        return True
    except subprocess.CalledProcessError:
        return False