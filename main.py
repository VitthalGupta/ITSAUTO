import subprocess
import platform
import time
import os
import sys

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
    var_file= open("var.txt","a")
    
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
try:
    from selenium import webdriver
    from selenium.webdriver.common.by import By
except ImportError as e:
    print("Installing Selenium")
    install("selenium")
    from selenium import webdriver
    from selenium.webdriver.common.by import By

# Check if wget is installed
if platform.system() == "Windows":
    if not os.path.exists("wget.exe"):
        print("Installing wget for Windows")
        install("wget")
elif platform.system() == "Linux":
    if os.system("wget --version") != 0:
        print("Installing wget for Linux")
        os.system("sudo apt-get install wget")
        import wget
    else:
        import wget
elif platform.system() == "Darwin":
    try:
        import wget
    except ImportError as e:
        print("Installing wget for Mac")
        install("wget")
        import wget

    


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
        options = options.Safari()
        driver = webdriver.Safari(options=options, executable_path='/usr/bin/safaridriver')

        userCredentials = {
            "username": "B319063",
            "password": "shyamsundergupta12"
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

# def algo_windows():
#     def login_windows():

# def algo_linux():

# Initialising the algorithm
os_detect()