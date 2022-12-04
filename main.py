import platform
import os
import argparse

# import check internet
from utility.check_internet import check_internet
# automatic updation of script will be enabled once a realease has been published
# from utility.update_script import check_release
from utility.update_var import update_var
from utility.fetch_data import fetch_var

# Importing algorithms
# from windows.windows import algo_window
from mac.mac import algo_mac
# from linux.linux import algo_linux

# Get the current working directory
from path import path, var_dir

# Creating a variable to store whether the algorithm is connected for the first time
var_dir = os.path.join(path, "var")
if os.path.exists(var_dir):
    pass
else:
    os.mkdir(var_dir)
    os.chdir(var_dir)
    var_file = open("var.txt", "w")
    var_file.write("Preferred network : ITS7000\nFirst time : True\nLogin time : 300\nauto-update : False\nPage Load Wait time : 20\nPage kill time : 5\nPackages installed : False\nCount : 1\nSelenium installed : False\nCryptography installed : False\nWget installed : False\nChrome driver installed : False\nChrome installed : False\nSafari driver installed : False\nSafari installed : False\nFirefox driver installed : False\nFirefox installed : False\nSafari Driver Enabled: False")
    var_file.close()
    os.chdir(path)

# Fetching the os name
os_name =platform.system()

# Initial check for internet connection
if check_internet(os_name):
    print("Internet connection is available")
else:
    print("Internet connection is not available")

# check from var if the algorithm is running for the first time
first_time = fetch_var("First time")
if first_time == "True":
    print("First time execution")
    print("Do you wish to auto-update (Y/n)")
    auto_update = input()
    if auto_update == "Y" or auto_update == "y":
        print("Auto update enabled")
        # update the variable file using update_var function
        update_var("auto-update : False", "auto-update : True")
    else:
        print("Auto update disabled")
        print("To update please run git pull")
    if not check_internet(os_name):
        print("Internet is needed to run the script for the first time")
        print("Please connect to the ITS and run the script again")
    update_var("First time : True", "First time : False")

# if auto update true then check for update
auto_update = fetch_var("auto-update")
if auto_update == "True":
    if check_internet(os_name):
        print("Checking for new releases")
        # check_release()

#Algorithm execution based on the os detected
def os_detect():
    if os_name == "Windows":
        print("Executing algorithm for Windows")
        # algo_window()
    elif os_name == "Linux":
        print("Executing algorithm for Linux")
        # algo_linux()
    elif os_name == "Darwin":
        print("Executing algorithm for Mac")
        algo_mac()
    else:
        print("OS not supported")

# Initialising the algorithm
if __name__ == '__main__':
    os_detect()