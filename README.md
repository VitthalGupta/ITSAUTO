# ITSAUTO
This repo will automate the authentication process for ITS for all available networks. We recommend you to ensure that 

## Required Packages
### Mac OS X
- [Python 3](https://www.python.org/)
- [pip](https://pip.pypa.io/en/stable/installing/)
- [git](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)

### Linux
- [Python 3](https://www.python.org/)
- [pip](https://pip.pypa.io/en/stable/installing/)
- [git](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)

### Windows
- [Python 3](https://www.python.org/)
- [pip](https://pip.pypa.io/en/stable/installing/)
- [git](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)

## Installation
- Clone the [repository](https://docs.github.com/en/repositories/creating-and-managing-repositories/cloning-a-repository) to your local machine.
- Open a terminal and [navigate](https://www.redhat.com/sysadmin/navigating-filesystem-linux-terminal) to the repository.
- Type 'python3 main.py' to run the program
- Internet is needed for the first time to install the required packages, connect to ITS network if you are running the script for thr first time.
- Depending on your system, you may need to use 'python' instead of 'python3'
- Dependecies will be installed automatically
- The script can be run in the background using [screen](https://www.howtogeek.com/662422/how-to-use-linuxs-screen-command/) (for linux and mac users only).
- You can also use [cron](https://opensource.com/article/17/11/how-use-cron-linux) to run the script at the time of startup, or at a specific time. (for linux and mac users only).

## Working -

# Step 1
    Detects the OS and installs the required dependencies.

# Step 2
    Detection of compatible network: 
    This process checks whether there is a compatible wifi connection available in proximity. In our use case this refers to any SSID with the prefix of "ITS".

# Step 3
    Connection to wifi: The algorithm followed here is, if the system finds a single SSID with the prefix ITS, then the application will check for the BSSID of the router having the strongest signal strength to the device.
    If your device can find multiple SSID's with the aforementioned prefix then the application will compare the signal strength of all the relevant BSSID's and then compare among the SSID's, this would determine the best SSID for connection. Then the router can be connected.

# Step 4
    Initialization of selenium and chrome driver module: This module will then initiate a headless chrome driver, the login id and the password would then be filled in the respective fields. After connecting the driver's tab will be closed.

# Step 5
    Reconnection after 5 mins: 
    This part would comprise of logging out of the network, by initializing the logout command in the url and connecting back using step 3.

## Note:
    Reconnection of wifi network connection may be applicable in case a better connection is discovered (in terms of signal of BSSID for the various SSID's available.)

## Developed by : -
### Vitthal Gupta - b319063@iiit-bh.ac.in
### Bignesh Sahoo - b319013@iiit-bh.ac.in