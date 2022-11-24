import platform
import os
import re
import getpass

# import check internet
from utility.check_internet import check_internet


 # import credentials
# from utility.credentials import Credentials
# # import install package
# from utility.install_package import install


# Importing algorithms

# from windows.windows import algo_window
from mac.mac import algo_mac
# from linux.linux import algo_linux

# Get the current working directory
from path import path, var_dir

# Initial check for internet connection
if check_internet():
    print("Internet connection is available")
else:
    print("Internet connection is required to install the required packages")
    print("Please connect to the internet and try again")

# Creating a variable to store whether the algorithm is connected for the first time
var_dir = os.path.join(path, "var")
if os.path.exists(var_dir):
    pass
else:
    os.mkdir(var_dir)
    os.chdir(var_dir)

    var_file = open("var.txt", "w")
    var_file.write("Login time: 300\nPackages installed : False\nSelenium installed : False\nCryptography installed : False\nWget installed : False\nChrome driver installed : False\nChrome installed : False\nSafari driver installed : False\nSafari installed : False\nFirefox driver installed : False\nFirefox installed : False\nInternet connection : False\nSafari Driver Enabled: False")
    var_file.close()
    os.chdir(path)

# creting a function to check if the algorithm is running for the first time
def first_time():
    os.chdir(var_dir)
    var_file = open("var.txt", "r")
    var_file_data = var_file.read()
    var_file.close()
    if re.search("Packages installed : False", var_file_data):
        print("Installing packages")
        os.chdir(path)
        return True
    else:
        print("Packages are already installed")
        os.chdir(path)



#Algorithm execution based on the os detected
def os_detect():
    os_name =platform.system()
    if os_name == "Windows":
        print("Executing algorithm for Windows")
        # algo_window
    elif os_name == "Linux":
        print("Executing algorithm for Linux")
        # algo_linux()
    elif os_name == "Darwin":
        print("Executing algorithm for Mac")
        algo_mac()
    else:
        print("OS not supported")

first_time()
# Initialising the algorithm
os_detect()