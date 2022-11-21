# ITSAUTO
Automation of firewall authentication of ITS.

## Working -

# Step 1
    Detection of compatible network: This process checks whether there is a compatible wifi connection available in proximity. In our use case this refers to any SSID with the prefix of  "ITS".

# Step 2
    Connection to wifi: The algorithm followed here is, if the system finds a single SSID with the prefix ITS, then the application will check for the BSSID of the router having the strongest signal strength to the device.
    If your device can find multiple SSID's with the aforementioned prefix then the application will compare the signal strength of all the relevant BSSID's and then compare among the SSID's, this would determine the best SSID for connection. Then the router can be connected.

# Step 3
    Initialization of selenium and chrome driver module: This module will then initiate a headless chrome driver, the login id and the password would then be filled in the respective fields. After connecting the driver's tab will be closed.

# Step 4
    Reconnection after 3600 secs: This part would comprise of logging out of the network, by initializing the logout command in the url and connecting back using step 3.

## Note:
    Reconnection of wifi network connection may be applicable in case a better connection is discovered (in terms of signal of BSSID for the various SSID's available.)

# Developed by (Alphabetical)
# Bignesh Sahoo - b319013@iiit-bh.ac.in
# Vitthal Gupta - b319063@iiit-bh.ac.in