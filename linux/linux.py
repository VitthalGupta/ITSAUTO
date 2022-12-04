import platform
import os
import sys
import getpass
import time
import subprocess

from utility.install_package import install
from utility.check_internet import check_internet_linux
from utility.credentials import Credentials
from utility.update_var import update_var
from utility.fetch_data import fetch_var

# get the dir route to main var file
from path import path, var_dir

print("Current working directory is: " + path)

def algo_linux():
    # Checking Selenium
    try:
        from selenium import webdriver
        from selenium.webdriver.common.by import By
        from selenium.webdriver.safari.options import Options
        from selenium.webdriver.common.keys import Keys
        from selenium.webdriver.support.ui import WebDriverWait

        # update the variable file
        update_var("Selenium installed : False", "Selenium installed : True")
    except ImportError as e:
        print("Installing Selenium")
        install("selenium")
        from selenium import webdriver
        from selenium.webdriver.common.by import By
        from selenium.webdriver.safari.options import Options
        from selenium.webdriver.common.keys import Keys
        from selenium.webdriver.support.ui import WebDriverWait
        # update the variable file
        update_var("Selenium installed : False", "Selenium installed : True")

    #Check if Cryptography is installed
    try:
        from cryptography.fernet import Fernet
        # update the variable file
        update_var("Cryptography installed : False",
                   "Cryptography installed : True")
    except ImportError as e:
        print("Installing Cryptography")
        install("cryptography")
        from cryptography.fernet import Fernet
        # update the variable file
        update_var("Cryptography installed : False",
                   "Cryptography installed : True")

    # check if chromedriver is downloaded
    if os.path.exists(os.path.join(path, "chromedriver")):
        print("Chromedriver is already downloaded")
        # update the variable file
        update_var("Chrome driver installed : False",
                   "Chrome driver installed : True")
    else:
        print("Downloading chromedriver")
        chrome_driver = os.path.join(path, "chromedriver")
        os.mkdir(chrome_driver)
        os.chdir(chrome_driver)
        os.system("wget https://chromedriver.storage.googleapis.com/2.46/chromedriver_linux64.zip")
        os.system("unzip chromedriver_linux64.zip")
        os.system("rm chromedriver_linux64.zip")
        # update the variable file
        update_var("Chrome driver installed : False",
                   "Chrome driver installed : True")
        os.chdir(path)
    
    # check if chrome is installed
    if os.path.exists("/usr/bin/google-chrome"):
        print("Chrome is already installed")
        # update the variable file
        update_var("Chrome installed : False", "Chrome installed : True")
    else:
        print("Installing Chrome")
        os.system("sudo apt-get install google-chrome-stable")
        # update the variable file
        update_var("Chrome installed : False", "Chrome installed : True")
    
    def login_linux():
        #fetch count from var file
        count = fetch_var("Count")
        print("Login count: " + str(count))
        # Fetching credentials from the  cred file
        os.chdir(path)
        cred_file = "cred"
        os.chdir(cred_file)
        cred_filename = 'CredFile.ini'

        key = ''
        with open('key.key', 'r') as key_in:
            key = key_in.read().encode()
        f = Fernet(key)

        with open(cred_filename, 'r') as cred_in:
            lines = cred_in.readlines()
            config = {}
            for line in lines:
                tuples = line.rstrip('\n').split('=', 1)
                if tuples[0] in ('Username', 'Password'):
                    config[tuples[0]] = tuples[1]
        passwd = f.decrypt(config['Password'].encode()).decode()
        os.chdir(path)

        # launch chrome web driver
        chrome_driver = os.path.join(path, "chromedriver")
        os.chdir(chrome_driver)
        chrome_options = Options()
        chrome_options.add_argument("--headless")
        chrome_options.add_argument("--window-size=1920x1080")
        driver = webdriver.Chrome(options=chrome_options)
        os.chdir(path)
        driver.get("https://192.168.1.250/connect")
        # wait for the page to load
        # fetch load page time from the var file
        load_page_time = fetch_var("Page Load Wait time")
        # time.sleep(int(load_page_time))
        # print(load_page_time)
        # reload if the page is not loaded within load_page_time secs

        try:
            WebDriverWait(driver, int(load_page_time)).until(
                lambda driver: driver.find_element("id", "LoginUserPassword_auth_username"))
            username = driver.find_element(
                "id", "LoginUserPassword_auth_username")
            # enter the username
            username.send_keys(config['Username'])
            # find the password field
            password = driver.find_element(
                "id", "LoginUserPassword_auth_password")
            # enter the password
            password.send_keys(passwd)
            # find the login button
            login = driver.find_element("id", "UserCheck_Login_Button_span")
            # click the login button
            login.click()
            # wait for the page to load
            # fetch kill page time from the var file
            kill_page_time = fetch_var("Page kill time")
            time.sleep(int(kill_page_time))
            # check if the login is successful
            if check_internet_linux():
                print("Login {} Successful".format(count))
            else:
                print("Login Failed")
                login_linux()
        except:
            driver.quit()
            os.chdir(path)
            print("Page not loaded within {} secs".format(load_page_time))
            print("Reloading the page")
            login_linux()
    
    # check available networks in linux
    available_its =[]
    devices = subprocess.check_output(
        ["/System/Library/PrivateFrameworks/Apple80211.framework/Versions/Current/Resources/airport", '-s'])
    devices = devices.decode('ascii')
    devices = devices.split("\n")
    for _ in devices:
        if (_.find("ITS") != -1):
            available_its.append(_.replace(" ", ""))
        #print(available_its)

     # Checking if credentials are present
    os.chdir(path)
    cred_file = "cred"
    if os.path.exists(cred_file):
        os.chdir(cred_file)
        cred_filename = 'CredFile.ini'
        if os.path.exists(cred_filename):
            print("Credentials file exists")
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
