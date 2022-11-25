import subprocess
import os
import re

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
    available_its_ssids = check_available_ssids()
    if(len(available_its_ssids)) == 0:
        print("No ITS networks found")
    else:
        try:
            subprocess.check_output(['netsh', 'wlan', 'connect', f'name={available_its_ssids[0]}'])
            print("Connected to ITS network")
        except subprocess.CalledProcessError:
            add_its_profile("ITS7000")
    


if __name__ == '__main__':
    algo_windows()
    # add_its_profile("ITS7000")