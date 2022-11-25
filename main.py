import platform
import os
import re

# import check internet
from utility.check_internet import check_internet
from utility.update_script import update_script, check_release
from utility.update_var import update_var

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
    # update_script()
else:
    print("Internet connection is not available")


# # Installing packages to update the script
# try:
#     from selfupdate import update
#     if check_internet():
#         update()
# except ImportError as e:
#     print("Installing selfupdate")
#     install("selfupdate")
#     from selfupdate import update
#     if check_internet():
#         update()


# Creating a variable to store whether the algorithm is connected for the first time
var_dir = os.path.join(path, "var")
if os.path.exists(var_dir):
    pass
else:
    os.mkdir(var_dir)
    os.chdir(var_dir)
    var_file = open("var.txt", "w")
    var_file.write("First time : True\nLogin time: 300\nauto-update : False\nPage Load Wait time : 20\nPage kill time : 5\nPackages installed : False\nCount : 1\nSelenium installed : False\nCryptography installed : False\nWget installed : False\nChrome driver installed : False\nChrome installed : False\nSafari driver installed : False\nSafari installed : False\nFirefox driver installed : False\nFirefox installed : False\nSafari Driver Enabled: False")
    var_file.close()
    os.chdir(path)

# check from var if the algorithm is running for the first time
os.chdir(var_dir)
var_file = open("var.txt", "r")
var_file_data = var_file.read()
var_file.close()
# search for the first time variable
first_time = re.search("First time : (.*)", var_file_data)
first_time = first_time.group(1)
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
    if not check_internet():
        print("Internet is needed to run the script for the first time")
        print("Please connect to the ITS and run the script again")
    update_var("First time : True", "First time : False")

# if auto update true then check for updates
os.chdir(var_dir)
var_file = open("var.txt", "r")
var_file_data = var_file.read()
var_file.close()
auto_update = re.search("auto-update : (.*)", var_file_data)
auto_update = auto_update.group(1)
if auto_update == "True":
    if check_internet():
        print("Checking for updates")
        # update_script()
        # print("Checking for new releases")
        # check_release()


#Algorithm execution based on the os detected
def os_detect():
    os_name =platform.system()
    if os_name == "Windows":
        print("Executing algorithm for Windows")
        # algo_window()
    elif os_name == "Linux":
        print("Executing algorithm for Linux")
        # # algo_linux()
    elif os_name == "Darwin":
        print("Executing algorithm for Mac")
        algo_mac()
    else:
        print("OS not supported")

# Initialising the algorithm
os_detect()