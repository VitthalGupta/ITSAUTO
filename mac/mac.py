import subprocess
import time
import sys
import os
import re
import getpass

from utility.install_package import install
from utility.check_internet import check_internet
from utility.credentials import Credentials


# get the dir route to main var file
from path import path, var_dir

print("Current working directory is: " + path)

def algo_mac():
    # Initial check for internet connection
    if check_internet():
        print("Internet connection is available")
    else:
        print("Internet connection is required to install the required packages")
        print("Please connect to the internet and try again")
        sys.exit()

    
    
    # Checking Selenium
    try:
        from selenium import webdriver
        from selenium.webdriver.common.by import By
        from selenium.webdriver.safari.options import Options
        from selenium.webdriver.common.keys import Keys

        # update the variable file
        os.chdir(var_dir)
        var_file = open("var.txt", "r")
        var_file_data = var_file.read()
        var_file.close()
        # check if the variable is already set to false
        if re.search("Selenium installed : False", var_file_data):
            var_file_data = re.sub("Selenium installed : False",
                                "Selenium installed : True", var_file_data)
            var_file = open("var.txt", "w")
            var_file.write(var_file_data)
            var_file.close()
        var_file.close()
        os.chdir(path)
    except ImportError as e:
        print("Installing Selenium")
        install("selenium")
        from selenium import webdriver
        from selenium.webdriver.common.by import By
        from selenium.webdriver.safari.options import Options
        from selenium.webdriver.common.keys import Keys
        os.chdir(var_dir)
        # check if selenium is installed

        var_file = open("var.txt", "r")
        var_file_data = var_file.read()
        var_file.close()
        var_file_data = re.sub("Selenium installed : False",
                            "Selenium installed : True", var_file_data)
        var_file = open("var.txt", "w")
        var_file.write(var_file_data)
        var_file.close()
        os.chdir(path)

        #Check if Cryptography is installed
    try:
        from cryptography.fernet import Fernet
        os.chdir(var_dir)
        var_file = open("var.txt", "r")
        var_file_data = var_file.read()
        var_file.close()
        var_file_data = re.sub("Cryptography installed : False",
                            "Cryptography installed : True", var_file_data)
        var_file = open("var.txt", "w")
        var_file.write(var_file_data)
        var_file.close()
        os.chdir(path)
    except ImportError as e:
        print("Installing Cryptography")
        install("cryptography")
        from cryptography.fernet import Fernet
        os.chdir(var_dir)
        var_file = open("var.txt", "r")
        var_file_data = var_file.read()
        var_file.close()
        var_file_data = re.sub("Cryptography installed : False",
                            "Cryptography installed : True", var_file_data)
        var_file = open("var.txt", "w")
        var_file.write(var_file_data)
        var_file.close()
        os.chdir(path)


    def login_mac():
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
        time.sleep(2)
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
        time.sleep(5)


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

    # variable to store the number of times the script has been run
    count = 1

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
    subprocess.check_output(
        ['networksetup', '-setairportnetwork', 'en0', only_its[0], 'iiitbbsr'])
    print("Connected to : {} ".format(only_its[0]))

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

    # update the variable file
    os.chdir(var_dir)
    var_file = open("var.txt", "r")
    var_file_data = var_file.read()
    var_file.close()
    # check if the variable is already set to false
    if re.search("Internet connection : False", var_file_data):
        var_file_data = re.sub("Internet connection : False",
                               "Internet connection : True", var_file_data)
        var_file = open("var.txt", "w")
        var_file.write(var_file_data)
        var_file.close()
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

    # logging in every 5 minutes
    while True:
        login_mac()
        count = count + 1
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
