import subprocess
import time
import sys
import os
import re
import getpass

from utility.install_package import install
from utility.check_internet import check_internet
from utility.credentials import Credentials
from utility.update_var import update_var


# get the dir route to main var file
from path import path, var_dir

print("Current working directory is: " + path)

def algo_mac():

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
        os.chdir(var_dir)
        # update the variable file
        update_var("Selenium installed : False", "Selenium installed : True")

        #Check if Cryptography is installed
    try:
        from cryptography.fernet import Fernet
        # update the variable file
        update_var("Cryptography installed : False", "Cryptography installed : True")
    except ImportError as e:
        print("Installing Cryptography")
        install("cryptography")
        from cryptography.fernet import Fernet
        # update the variable file
        update_var("Cryptography installed : False", "Cryptography installed : True")


    def login_mac():
        #fetch count from var file
        os.chdir(var_dir)
        var_file = open("var.txt", "r")
        var_file_data = var_file.read()
        var_file.close()
        count = re.search("Count : (.*)", var_file_data)
        count = count.group(1)
        print("Logging in  " + str(count)  + " time")
        # Fetching credentials from the  cred file
        os.chdir(path)
        cred_file = "cred"
        os.chdir(cred_file)
        cred_filename = 'CredFile.ini'
        # read username from the cred file using configparser
        # config = configparser.ConfigParser()
        # config.read(cred_filename)
        # username = config['Cred']['username']

        # key_file= 'key.key'
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
        # print(config)
        passwd = f.decrypt(config['Password'].encode()).decode()
        # config = configparser.ConfigParser()
        # config.read(cred_filename)
        # username_id = config['DEFAULT']['Username']
        # password_id = config['DEFAULT']['Password']
        # # Fetching the key from the key file
        # key_file = 'key.key'
        # with open(key_file, 'r') as key_in:
        #     key = key_in.read().encode()
        # f = Fernet(key)
        # password = f.decrypt(password.encode()).decode()
        # del f
        os.chdir(path)

        # launch safari web browser and loging in 

        driver = webdriver.Safari()
        driver.get("https://192.168.1.250/connect")
        # wait for the page to load
        # fetch load page time from the var file
        os.chdir(var_dir)
        var_file = open("var.txt", "r")
        var_file_data = var_file.read()
        var_file.close()
        load_page_time = re.search("Page Load Wait time : (.*)", var_file_data)
        load_page_time = load_page_time.group(1)
        load_page_time = int(load_page_time)
        
        # reload if the page is not loaded within 10 secs
        try: 
            WebDriverWait(driver, load_page_time).until(
                lambda driver: driver.find_element("id", "LoginUserPassword_auth_username"))
            # find the username field
            username = driver.find_element("id","LoginUserPassword_auth_username")
            # enter the username
            username.send_keys(config['Username'])
            # find the password field
            password = driver.find_element("id","LoginUserPassword_auth_password")
            # enter the password
            password.send_keys(passwd)
            # find the login button
            login = driver.find_element("id","UserCheck_Login_Button_span")
            # click the login button
            login.click()
            # wait for the page to load
            # fetch kill page time from the var file
            os.chdir(var_dir)
            var_file = open("var.txt", "r")
            var_file_data = var_file.read()
            var_file.close()
            kill_page_time = re.search("Page kill time : (.*)", var_file_data)
            kill_page_time = kill_page_time.group(1)
            kill_page_time = int(kill_page_time)
            time.sleep(kill_page_time)
            os.chdir(path)
            # check if the login is successful
            if not check_internet():
                print("Login Failed")
                login_mac()
        except:
            driver.quit()
            os.chdir(path)
            print("Page not loaded within {} secs".format(load_page_time))
            print("Reloading the page")
            login_mac()


    # Check available connections
    available_its = []
    devices = subprocess.check_output(
        ["/System/Library/PrivateFrameworks/Apple80211.framework/Versions/Current/Resources/airport", '-s'])
    devices = devices.decode('ascii')
    devices = devices.split("\n")
    for _ in devices:
        if (_.find("ITS") != -1):
            available_its.append(_.replace(" ", ""))
        #print(available_its)


    #filtering data
    only_its = []
    its = []
    for _ in available_its:
        its = _.split("-")
        if its[0] not in only_its:
            only_its.append(its[0])

    # Printing availble SSID's
    print("Available SSID'S: ")
    for _ in only_its:
        print(_)

    # Connect to the network {networksetup -setairportnetwork en0 <SSID_OF_NETWORK> <PASSWORD>}
    # only_its in not empty
    if len(only_its) != 0:
        subprocess.check_output(
            ['networksetup', '-setairportnetwork', 'en0', only_its[0], 'iiitbbsr'])
        print("Connected to : {} ".format(only_its[0]))
    else: 
        print("No ITS available")
        algo_mac()

#    # Enbling safari driver for mac and updating the var file
#     print("Checking if Safari driver is enabled")
#     os.chdir(var_dir)
#     var_file = 'var.txt'
#     # Finding Safari driver status in var file

#     with open(var_file, 'r') as var_in:
#         var = var_in.read()
#     # Safari driver enble if false

#     if var == '0':
#         print("Enabling Safari driver")
#         print('Enter the system password')
#         os.system("sudo safaridriver --enable")

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

    # Update var file for install all packages
    update_var("Install all packages : False", "Install all packages : True")
    
    # Update var file for safari driver
    update_var("Safari driver installed : False", "Safari driver installed : True")
    
    # Update var file for safari browser
    update_var("Safari installed : False", "Safari installed : True")

    # logging in every 5 minutes
    while True:
        login_mac()
        # update count from var file
        os.chdir(var_dir)
        var_file = open("var.txt", "r")
        var_file_data = var_file.read()
        var_file.close()
        count = re.search("Count : (.*)", var_file_data)
        count = count.group(1)
        count = int(count)
        count += 1
        # update count in var file
        update_var("Count : {}".format(count - 1), "Count : {}".format(count))
        # get the time duration from var file
        os.chdir(var_dir)
        var_file = 'var.txt'
        os.chdir(var_dir)
        var_file = open("var.txt", "r")
        var_file_data = var_file.read()
        var_file.close()
        login_time = re.search("Login time: (.*)", var_file_data).group(1)
        os.chdir(path)
        time.sleep(int(login_time))
