import subprocess
import platform
import time
import os
import sys
import re
import ctypes
import getpass
import configparser

# Checking for internet connection
def check_internet():
    try:
        subprocess.check_output(["ping", "www.google.com", "-c", "3"])
        return True
    except subprocess.CalledProcessError:
        return False


# Get the current working directory
path = os.getcwd()
print("Current working directory is: " + path)

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


# Initial check for internet connection
if check_internet():
    print("Internet connection is available")
else:
    print("Internet connection is required to install the required packages")
    print("Please connect to the internet and try again")

# Function to install the required packages
def install(package):
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])

# Check if the required packages are installed

# Selenium
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
    var_file_data = re.sub("Selenium installed : False", "Selenium installed : True", var_file_data)
    var_file = open("var.txt", "w")
    var_file.write(var_file_data)
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
    var_file = open("var.txt", "r")
    var_file_data = var_file.read()
    var_file.close()
    var_file_data = re.sub("Selenium installed : False",
                           "Selenium installed : True", var_file_data)
    var_file = open("var.txt", "w")
    var_file.write(var_file_data)
    var_file.close()
    os.chdir(path)

# # check if selenium server is downloaded
# Selenium server is not needed for standalone tasks
# selenium_dir = os.path.join(path, "selenium")
# if os.path.exists(selenium_dir):
#     print("Selenium server is already downloaded")
# else:
#     print("Downloading Selenium server")
#     os.mkdir(selenium_dir)
#     os.chdir(selenium_dir)
#     subprocess.check_call(["curl", "-O", "https://selenium-release.storage.googleapis.com/3.141/selenium-server-standalone-3.141.59.jar"])
#     os.chdir(path) 

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

# Check if wget is installed
if platform.system() == "Windows":
    if not os.path.exists("wget.exe"):
        print("Installing wget for Windows")
        install("wget")
        # update the variable file
        os.chdir(var_dir)
        var_file = open("var.txt", "r")
        var_file_data = var_file.read()
        var_file.close()
        var_file_data = re.sub("Wget installed : False", "Wget installed : True", var_file_data)
        var_file = open("var.txt", "w")
        var_file.write(var_file_data)
        var_file.close()
        os.chdir(path)
    else:
        print("wget is already installed")
        os.chdir(var_dir)
        var_file = open("var.txt", "r")
        var_file_data = var_file.read()
        var_file.close()
        var_file_data = re.sub("Wget installed : False",
                               "Wget installed : True", var_file_data)
        var_file = open("var.txt", "w")
        var_file.write(var_file_data)
        var_file.close()
        os.chdir(path)
elif platform.system() == "Linux":
    if os.system("wget --version") != 0:
        print("Installing wget for Linux")
        os.system("sudo apt-get install wget")
        import wget
        os.chdir(var_dir)
        var_file = open("var.txt", "r")
        var_file_data = var_file.read()
        var_file.close()
        var_file_data = re.sub("Wget installed : False",
                               "Wget installed : True", var_file_data)
        var_file = open("var.txt", "w")
        var_file.write(var_file_data)
        var_file.close()
        os.chdir(path)
    else:
        import wget
        print("wget is already installed")
        os.chdir(var_dir)
        var_file = open("var.txt", "r")
        var_file_data = var_file.read()
        var_file.close()
        var_file_data = re.sub("Wget installed : False",
                               "Wget installed : True", var_file_data)
        var_file = open("var.txt", "w")
        var_file.write(var_file_data)
        var_file.close()
        os.chdir(path)
elif platform.system() == "Darwin":
    try:
        import wget
        os.chdir(var_dir)
        var_file = open("var.txt", "r")
        var_file_data = var_file.read()
        var_file.close()
        var_file_data = re.sub("Wget installed : False",
                               "Wget installed : True", var_file_data)
        var_file = open("var.txt", "w")
        var_file.write(var_file_data)
        var_file.close()
        os.chdir(path)
    except ImportError as e:
        print("Installing wget for Mac")
        install("wget")
        import wget
        os.chdir(var_dir)
        var_file = open("var.txt", "r")
        var_file_data = var_file.read()
        var_file.close()
        var_file_data = re.sub("Wget installed : False",
                               "Wget installed : True", var_file_data)
        var_file = open("var.txt", "w")
        var_file.write(var_file_data)
        var_file.close()
        os.chdir(path)

    


# Checking and downloading ChromeDriver
fd_list = os.listdir(path)
ch_directory = 'chromedriver'
if 'chromedriver' in fd_list:
    print("ChromeDriver is already downloaded")
else:
    ch_path = os.path.join(path, ch_directory)
    print("Creating a directory for ChromeDriver")
    os.mkdir(ch_path)
    os.chdir(ch_path)
    print("Downloading ChromeDriver")
    if platform.system() == "Windows":
        print("Downloading ChromeDriver for Windows")
        wget.download("https://chromedriver.storage.googleapis.com/2.41/chromedriver_win32.zip")
    elif platform.system() == "Linux":
        print("Downloading ChromeDriver for Linux")
        wget.download("https://chromedriver.storage.googleapis.com/2.41/chromedriver_linux64.zip")
    elif platform.system() == "Darwin":
        print("Downloading ChromeDriver for Mac")
        wget.download("https://chromedriver.storage.googleapis.com/2.41/chromedriver_mac64.zip")

    print("Unzipping ChromeDriver")
    if platform.system() == "Windows":
        os.system("unzip chromedriver_win32.zip")
        os.remove("chromedriver_win32.zip")
        
    elif platform.system() == "Linux":
        os.system("unzip chromedriver_linux64.zip")
        os.remove("chromedriver_linux64.zip")
    elif platform.system() == "Darwin":
        os.system("unzip chromedriver_mac64.zip")
        os.remove("chromedriver_mac64.zip")
    print("ChromeDriver is downloaded")
    # update the variable file
    os.chdir(var_dir)
    var_file = open("var.txt", "r")
    var_file_data = var_file.read()
    var_file.close()
    var_file_data = re.sub("ChromeDriver installed : False",
                           "ChromeDriver installed : True", var_file_data)
    var_file = open("var.txt", "w")
    var_file.write(var_file_data)
    var_file.close()
    os.chdir(path)


# Class defination for credentials
class Credentials():
    def __init__(self):
        self.__username = ""
        self.__key = ""
        self.__password = ""
        self.__key_file = 'key.key'
        self.__time_of_exp = -1

    @property
    def password(self):
        return self.__password

    @password.setter
    def password(self, password):
        self.__key = Fernet.generate_key()
        f = Fernet(self.__key)
        self.__password = f.encrypt(password.encode()).decode()
        del f

    @property
    def username(self):
        return self.__username

    @username.setter
    def username(self, username):
        while (username == ''):
            username = input(
                'Enter a proper User name, blank is not accepted:')
        self.__username = username
    
    def create_cred(self):
        os.chdir(path)
        cred_file = "cred"
        if os.path.exists(cred_file):
            print("Credentials file already exists")
        else:
            os.mkdir(cred_file)
            os.chdir(cred_file)
            cred_filename = 'CredFile.ini'
            with open(cred_filename, 'w') as file_in:
                file_in.write("#Credential file:\nUsername={}\nPassword={}\n"
                            .format(self.__username, self.__password))
                file_in.write("++"*20)
        #If there exists an older key file, This will remove it.
        if (os.path.exists(self.__key_file)):
            os.remove(self.__key_file)
        #Open the Key.key file and place the key in it.
        #The key file is hidden.
        try:
            os_name = platform.system()
            # creating the key file
            with open(self.__key_file, 'w') as key_in:
                key_in.write(self.__key.decode())
            # Hiding the key file
            if (os_name == "Windows"):
                os.system("attrib +h key.key")
            elif (os_name == "Linux"):
                os.system("chmod 600 key.key")
            elif (os_name == "Darwin"):
                os.system("chmod 600 key.key")
            

        except PermissionError as e:
            print("Permission denied to hide the key file")
            print("Please run the program as an administrator")
        
        self.__username = ""
        self.__password = ""
        self.__key = ""
        self.__key_file

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

        # Fetching credentials from the  cred file
        os.chdir(path)
        cred_file = "cred"
        os.chdir(cred_file)
        cred_filename = 'CredFile.ini'
        config = configparser.ConfigParser()
        config.read(cred_filename)
        username_id = config['DEFAULT']['Username']
        password_id = config['DEFAULT']['Password']
        # Fetching the key from the key file
        key_file = 'key.key'
        with open(key_file, 'r') as key_in:
            key = key_in.read().encode()
        f = Fernet(key)
        password = f.decrypt(password.encode()).decode()
        del f
        os.chdir(path)

        # launch safari web browser
        driver = webdriver.Safari()
        driver.get("https://192.168.1.250/connect")
        # wait for the page to load
        time.sleep(5)
        # find the username field
        username = driver.find_element_by_id("LoginUserPassword_auth_username")
        # enter the username
        username.send_keys(cred.username)
        # find the password field
        password = driver.find_element_by_id("LoginUserPassword_auth_password")
        # enter the password
        password.send_keys(cred.password)
        # find the login button
        login = driver.find_element_by_id("UserCheck_Login_Button_span")
        # click the login button
        login.click()
        # wait for the page to load
        time.sleep(5)
        
        # Logging in
        try:
            driver.get("https://192.168.1.250/connect/")

            # submitBtn = driver.find_element(By.TAG_NAME, "input")
            # submitBtn.click()

            # redirectBtn = driver.find_element(By.ID, "openPortalLoginPageButton")
            # redirectBtn.click()

            username = driver.find_element(By.ID, "un")
            password = driver.find_element(By.ID, "pd")
            submitBtn = driver.find_element_by_css_selector("body > div > div > form > div:nth-child(7) > input[type=submit]")

            # print(submitBtn)

            username.send_keys(username_id)
            password.send_keys(password_id)
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
        

    # Checking if credentials are present

    os.chdir(path)
    cred_file = "cred"
    if os.path.exists(cred_file):
        os.chdir(cred_file)
        cred_filename = 'CredFile.ini'
        if os.path.exists(cred_filename):
            print("Credentials file exists")
            login_mac()
        else:
            print("Credentials file does not exist")
            print("Creating credentials file")
            cred = Credentials()
            cred.username = input("Enter your username: ")
            cred.password = getpass.getpass("Enter your password: ")
            cred.create_cred()
            login_mac()
    else:
        print("Credentials file does not exist")
        print("Creating credentials file")
        cred = Credentials()
        cred.username = input("Enter your username: ")
        cred.password = getpass.getpass("Enter your password: ")
        cred.create_cred()
        login_mac()


# def algo_windows():
#     def login_windows():

# def algo_linux():

# Initialising the algorithm
os_detect()