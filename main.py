from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.common.by import By
import subprocess

def check_its_strength(available_its):
    pass


def login():
    options = ChromeOptions()
    driver = webdriver.Chrome(options=options)
    driver.get("http://gstatic.com/generate_204")

    # submitBtn = driver.find_element(By.TAG_NAME, "input")
    # submitBtn.click()

    # redirectBtn = driver.find_element(By.ID, "openPortalLoginPageButton")
    # redirectBtn.click()

    username = driver.find_element(By.ID, "un")
    password = driver.find_element(By.ID, "pd")
    # submitBtn = driver.find_element(By.TAG_NAME, "input")
    submitBtn = driver.find_element_by_css_selector("body > div > div > form > div:nth-child(7) > input[type=submit]")

    print(submitBtn)

    userCredentials = {
        "username": "B320063",
        "password": "B320063"
    }

    username.send_keys(userCredentials["username"])
    password.send_keys(userCredentials["password"])
    submitBtn.click()


# Check available connections
available_its = []
devices = subprocess.check_output(
    ['netsh', 'wlan', 'show', 'networks', "mode=bssid"])
devices = devices.decode('ascii')
# devices = devices.replace("\r", "")
# devices = devices.replace("\n", "")
# devices = devices.replace(" ", "")
devices = devices.split("\r\n\r\n")
# for _ in devices:
#     print(_, sep="test\n")

# print(devices)
for _ in devices:
    if(_.find("ITS") != -1):
        available_its.append(_)
print(available_its)

if(len(available_its) == 1):
    subprocess.check_output(['netsh', 'wlan', 'connect', 'name=ITS700'])
    login()
else:
    check_its_strength(available_its)


# if __name__ == '__main__':
#     connect()
