import subprocess
import os
import re
import sys

sys.path.append("..")

from utility.check_internet import check_internet

path = os.getcwd()

def setup():
    '''
    This function is used to setup the script and install required dependencies when invoked for the first time on user's system.
    '''
    print("Checking dependencies...")

    # Creating a variable to store whether the algorithm is connected for the first time
    var_dir = os.path.join(path, "var")
    if os.path.exists(var_dir):
        pass
    else:
        os.mkdir(var_dir)
        os.chdir(var_dir)
        var_file= open("var.txt","w")
        var_file.write("Packages installed : False\nSelenium installed : False\nCryptography installed : False\nWget installed : False\nChrome driver installed : False\nChrome installed : False\nSafari driver installed : False\nSafari installed : False\nFirefox driver installed : False\nFirefox installed : False\nInternet connection : False\nSafari Driver Enabled: False")
        var_file.close()
        os.chdir(path)

    def check_true_dependencies():
        with open(f"{var_dir}/var.txt", "r") as f:
            for line in f:
                if line.find("False"):
                    return False
            return True
            
    if check_true_dependencies() == True:
        pass
    elif check_internet():
        print("Connected to internet. Checking for missing dependencies")
    else:
        print("An internet connection is required to install. Kindly connect to the internet and try again.")

    

def add_its_profile(ssid, key="iiitbbsr"):
    '''
    This function is used for adding the network profile for ITS to windows' network profiles when connecting to ITS for the first time
    '''
    print(f"Creating new SSID profile for {ssid}")
    with open(f"{ssid}_profile.xml", "w") as f1, open("profile_template.txt", "r") as f2:
        for line in f2:
            f1.write(line)

    with open(f"{ssid}_profile.xml", "r") as f1:
        data = f1.read()
        data = data.replace("{SSID}", ssid)
        data = data.replace("{password}", key)

    with open(f"{ssid}_profile.xml", "w") as f1:
        f1.write(data)

    print(f"Adding {ssid} to Windows' network profiles.")
    subprocess.check_output(["netsh", "wlan", "add", "profile", f"filename={ssid}_profile.xml"], shell=True)
    print(f"Successfully added {ssid} to Windows' network profiles'")
    
    # Deleting the network profile file
    os.remove(f"{ssid}_profile.xml")

def connect():
    pass



def check_available_ssids():
    # Get a list of available SSIDs
    available_its = []
    available_its_ssids = []
    ssids = subprocess.check_output(["netsh", "wlan", "show", "networks", "mode=bssid"])
    ssids = ssids.decode("ascii")
    ssids = ssids.split("\r\n\r\n")

    for _ in ssids:
        if(_.find("ITS") != -1):
            available_its.append(_.replace(" ", ""))

    for _ in available_its:
        res = _.split("\r\n")
        available_its_ssids.append(res[0][6:])

    return available_its_ssids

def algo_windows():
    setup()
    available_its_ssids = check_available_ssids()
    if(len(available_its_ssids)) == 0:
        print("No ITS networks found")
    else:
        try:
            subprocess.check_output(['netsh', 'wlan', 'connect', f'name={available_its_ssids[0]}'])
            print(f"Connected to {available_its_ssids[0]} network")
            connect()
        except subprocess.CalledProcessError:
            add_its_profile("ITS7000")
            connect()
    


if __name__ == '__main__':
    algo_windows()