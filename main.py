import platform
import os
import argparse

# import check internet
from utility.check_internet import check_internet
# automatic updation of script will be enabled once a realease has been published
# from utility.update_script import check_release
from utility.update_var import update_var
from utility.fetch_data import fetch_var
from utility.install_package import install

# importing scripts
from windows.windows import algo_windows
from mac.mac import algo_mac
from linux.linux import algo_linux

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
    var_file.write("Preferred network : ITS7000\nFirst time : True\nLogin time : 40000\nauto-update : False\nPage Load Wait time : 10\nPage kill time : 2\nPackages installed : False\nCount : 1\nSelenium installed : False\nCryptography installed : False\nWget installed : False\nChrome driver installed : False\nChrome installed : False\nSafari driver installed : False\nSafari installed : False\nFirefox driver installed : False\nFirefox installed : False\nSafari Driver Enabled: False")
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
# Starts the setup for first time installation
first_time = bool(fetch_var("First time"))
if first_time == "True":
    print("Script Configuration :")
    print("Installing Cryptography")
    install("cryptography")
    print("Do you wish to auto-update (Y/n)")
    auto_update = input()
    if auto_update == "Y" or auto_update == "y":
        print("Auto update enabled")
        # update the variable file using update_var function
        update_var("auto-update : False", "auto-update : True")
    else:
        print("Auto update disabled")
        print("To update please run git pull, or change it from var.txt")
    if not check_internet(os_name):
        print("Internet is needed to run the script for the first time")
        print("Please connect to the ITS and run the script again")
    preferred_ssid = "ITS7000"
    print("Please type a preferred ITS Network (default: ITS7000) :")
    preferred_ssid = input()
    preferred_ssid.replace(" ","")
    if preferred_ssid != "ITS7000":
        update_var("Preferred network : ITS7000", "Preferred network : {}".format(preferred_ssid))
    print("Setup login wait time (default: 300 secs)")
    print("Login wait time will setup the relogin period in seconds.")
    login_time=300
    login_time = input()
    if login_time != 300:
        update_var("Login time : 300","Login time : {}".format(login_time))
    print("Setup wait time for page loading (deafult: 10 secs)")
    page_load_time = 20
    page_load_time = input()
    if page_load_time!= 20:
        update_var("Page Load Wait time : 20", "Page Load Wait time : {}".format(page_load_time))
    print("Setup Page kill time (default: 2 secs)")
    page_kill_time = 2
    page_kill_time = input()
    if page_kill_time!= 2:
        update_var("Page kill time : 2", "Page kill time : {}".format(page_kill_time))
    
    update_var("First time : True", "First time : False")

# # if auto update true then check for update
# auto_update = fetch_var("auto-update")
# if auto_update == "True":
#     if check_internet(os_name):
#         print("Checking for new releases")
#         # check_release()

#Algorithm execution based on the os detected
def os_detect():
    if os_name == "Windows":
        print("Executing algorithm for Windows")
        algo_windows()
    elif os_name == "Linux":
        print("Executing algorithm for Linux")
        algo_linux()
    elif os_name == "Darwin":
        print("Executing algorithm for Mac")
        algo_mac()
    else:
        print("Operating System detected by the script is not compatible.")

# Initialising the algorithm
if __name__ == '__main__':
    os_detect()