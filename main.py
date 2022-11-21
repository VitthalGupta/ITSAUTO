from selenium import webdriver
from selenium.webdriver.common.by import By
import subprocess
import platform
import time

#Algorithm execution based on the os detected
def os_detect():
    os_name =platform.system()
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
        print("OS not supported")

def algo_mac():
    def login_mac():
        options = Options.Safari()
        driver = webdriver.Safari(options=options, executable_path='/Users/vitthal/Documents/GitHub/ITSAUTO/chromedriver')

        userCredentials = {
            "username": "B320063",
            "password": "B320063"
        }

        try:
            driver.get("http://gstatic.com/generate_204")

            # submitBtn = driver.find_element(By.TAG_NAME, "input")
            # submitBtn.click()

            # redirectBtn = driver.find_element(By.ID, "openPortalLoginPageButton")
            # redirectBtn.click()

            username = driver.find_element(By.ID, "un")
            password = driver.find_element(By.ID, "pd")
            submitBtn = driver.find_element_by_css_selector("body > div > div > form > div:nth-child(7) > input[type=submit]")

            # print(submitBtn)

            username.send_keys(userCredentials["username"])
            password.send_keys(userCredentials["password"])
            submitBtn.click()
        
        except:
            print("Error logging in to the wifi network")

        else:
            pass



    # Check available connections
    available_its = []
    devices = subprocess.check_output(["/System/Library/PrivateFrameworks/Apple80211.framework/Versions/Current/Resources/airport",'-s'])
    devices = devices.decode('ascii')
    devices = devices.split("\n")
    for _ in devices:
            if(_.find("ITS") != -1):
                available_its.append(_.replace(" ",""))
        #print(available_its)

    #filtering data
    only_its = []
    its = []
    for _ in available_its:
        its =_.split("-")
        if its[0] not in only_its:
            only_its.append(its[0])

    # Printing availbale SSID's
    print("Available SSID'S: ")
    for _ in only_its:
            print(_)

    # Connect to the network {networksetup -setairportnetwork en0 <SSID_OF_NETWORK> <PASSWORD>}
    subprocess.check_output(['networksetup', '-setairportnetwork', 'en0',only_its[0], 'iiitbbsr'])
    login_mac()

os_detect()