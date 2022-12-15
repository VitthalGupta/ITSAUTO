import subprocess
import os
import re
import sys
import zipfile
import getpass
import time
import copy

from cryptography.fernet import Fernet

sys.path.append(".")
sys.path.append("..")

from utility.check_internet import check_internet_windows
from utility.install_package import install
from utility.credentials import Credentials

from path import path, var_dir, cred_dir


def setup():
    '''
    This function is used to setup the script and install required dependencies when invoked for the first time on user's system.
    '''
    print("Checking dependencies...")

    # Creating a variable to store whether the algorithm is connected for the first time
    # var_dir = os.path.join(path, "var")
    if os.path.exists(var_dir):
        pass
    else:
        print(var_dir)
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
    elif check_internet_windows() == True:
        print("Connected to internet. Checking for missing dependencies")
    else:
        print("An internet connection is required to install. Kindly connect to the internet and try again.")
        sys.exit("Script terminated")

    # checking for selenium packages
    try:
        from selenium import webdriver
        from selenium.webdriver.common.by import By
        from selenium.webdriver.common.keys import Keys


    except ImportError:
        print("Selenium not installed")
        print("Installing Selenium")
        install("selenium")
    
    finally:
        os.chdir(var_dir)
        with open("var.txt","r") as f:
            file_data = f.read()
            if(re.search("Selenium installed : False", file_data)):
                file_data = re.sub("Selenium installed : False", "Selenium installed : True", file_data)
        
        with open("var.txt", "w") as f:
            f.write(file_data)
        os.chdir(path)

    # checking for Cryptography package installed
    try:
        from cryptography.fernet import Fernet
    except ImportError:
        print("Cryptography not installed")
        print("Installing Cryptography")
        install("cryptography")
    finally:
        os.chdir(var_dir)
        with open("var.txt","r") as f:
            file_data = f.read()
            if(re.search("Cryptography installed : False", file_data)):
                file_data = re.sub("Cryptography installed : False", "Cryptography installed : True", file_data)
        
        with open("var.txt", "w") as f:
            f.write(file_data)
        os.chdir(path)

    # checking for wget package installed
    # try:
    #     import wget
    # except ImportError:
    #     print("Wget not installed")
    #     print("Installing Wget")
    #     install("wget")
    # finally:
    #     os.chdir(var_dir)
    #     with open("var.txt","r") as f:
    #         file_data = f.read()
    #         if(re.search("Wget installed : False", file_data)):
    #             file_data = re.sub("Wget installed : False", "Wget installed : True", file_data)
        
    #     with open("var.txt", "w") as f:
    #         f.write(file_data)
    #     os.chdir(path)
    
    # checking if Chromedriver is available or not
    if os.path.exists(f"{path}/chromedriver/chromedriver.exe"):
        pass
    else:
        import requests
        chrome_driver_url = "https://chromedriver.storage.googleapis.com/107.0.5304.62/chromedriver_win32.zip"
        print("Downloading Chrome Driver")
        r = requests.get(chrome_driver_url)
        with open("chromedriver.zip", 'wb') as fd:
            for chunk in r.iter_content(chunk_size=128):
                fd.write(chunk)

        print("Extracting Chrome Driver")
        with zipfile.ZipFile("chromedriver.zip", 'r') as zip_ref:
            zip_ref.extractall("chromedriver")

        os.remove("chromedriver.zip")


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

def check_credentials_file():
    os.chdir(path)
    if os.path.exists(cred_dir):
        cred_filename = "CredFile.ini"
        if os.path.exists(f"{cred_dir}/{cred_filename}"):
            print("Credential file exists. Logging in...")
            return
        else:
            print("Credentials file does not exist")
            print("Creating credentials file")
            cred = Credentials()
            cred.username = input("Enter your username: ")
            cred.password = getpass.getpass("Enter your password: ")
            cred.create_cred()
    else:
        print("Credentials file does not exist")
        print("Creating credentials file")
        cred = Credentials()
        cred.username = input("Enter your username: ")
        cred.password = getpass.getpass("Enter your password: ")
        cred.create_cred()

def reading_credentials_file():
    '''
    Read credentials file and return username and password
    '''
    cred_filename = "CredFile.ini"
    key_filename = "key.key"
    os.chdir(cred_dir)

    with open(key_filename, 'r') as key_f:
        key = key_f.read().encode()
    
    f = Fernet(key)

    with open(cred_filename, 'r') as cred_f:
        cred_lines = cred_f.readlines()
        user_auth = {}

        for line in cred_lines:
            line = line.strip()
            if line.startswith("Username"):
                username = line.split("=",1)[1].strip(" \n")
                user_auth["username"] = username
            if line.startswith("Password"):
                password = line.split("=",1)[1].strip("\n")
                # user_auth["password"] = password
                # print(password)
                user_auth["password"] = f.decrypt(password.encode()).decode()

    # pd = f.decrypt(user_auth["password"].encode()).decode()
    # print(pd)
    os.chdir(path)
    return user_auth

def connect():
    check_credentials_file()
    user_auth = reading_credentials_file()

    os.chdir(var_dir)
    with open("var.txt","r") as f:
        var_file_data = f.read()
        count = re.search("Count" + " : (.*)", var_file_data)
        count = count.group(1)
    print("Login count: " + str(count))

    from selenium import webdriver
    from selenium.webdriver.common.keys import Keys
    from selenium.webdriver.common.by import By
    from selenium.webdriver.support.wait import WebDriverWait
    from selenium.webdriver.support import expected_conditions as EC
    from selenium.webdriver.chrome.options import Options
    chrome_options = Options()
    # Make the entire operation headless to reduce memory usage
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--window-size=1920,1080")

    os.chdir(var_dir)
    with open("var.txt", "r") as f:
        var_file_data = f.read()
        load_page_time = re.search("Page Load Wait time" + " : (.*)", var_file_data)
        # print(int(load_page_time))
        load_page_time = load_page_time.group(1)
        kill_page_time = re.search("Page kill time" + " : (.*)", var_file_data)
        kill_page_time = kill_page_time.group(1)

    try:
        driver = webdriver.Chrome(f"{path}/chromedriver/chromedriver.exe")
        driver.get("https://192.168.1.250/connect")

        try:
            # Below code block is used to bypass the warning issued by Chrome that the connection is not private and
            WebDriverWait(driver, 5).until(
                EC.presence_of_element_located((By.ID, "details-button"))
            )
            adv_btn = driver.find_element(By.ID, "details-button")
            adv_btn.click()
            proceed_btn = driver.find_element(By.ID, "proceed-link")
            proceed_btn.click()
            
            WebDriverWait(driver, load_page_time).until(
                EC.presence_of_element_located((By.ID, "LoginUserPassword_auth_password"))
            )
            un = driver.find_element(By.ID, "LoginUserPassword_auth_username")
            un.send_keys(user_auth["username"])

            pw = driver.find_element(By.ID, "LoginUserPassword_auth_password")
            # pw.send_keys(user_auth["key"].decrypt(user_auth["password"].encode()).decode())
            pw.send_keys(user_auth["password"])

            login = driver.find_element(By.ID, "UserCheck_Login_Button_span")
            login.click()

            time.sleep(kill_page_time)

            if check_internet_windows():
                print("Successfully logged in!")
            else:
                print("Login Failed. Logging in again...")
                connect()

        except Exception as e:
            print(e)
            driver.quit()
            print("There was some issue in logging in. Trying again...")
            connect()
    
    except Exception as e:
        print(e)
        driver.quit()
        print("There was some issue in logging in. Trying again...")
        connect()


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
            add_its_profile(available_its_ssids[0])
            connect()
    


if __name__ == '__main__':
    algo_windows()