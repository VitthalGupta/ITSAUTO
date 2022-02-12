# ITSAUTO
Automation of firewall authentication of ITS.

## How this scripts works -

# Step 1
    Detection of compatible network: This process checks whether there is a compatible wifi connection available in proximity. In our use case this refers to any SSID with the prefix of  "ITS".

# Step 2
    Connection to wifi: The algorithm followed here is if the system finds a single SSID with the prefix ITS, then the application will check for the BSSID of the router having the strongest signal strength to the device.
    If your device can find multiple SSID's with the aforementioned prefix then the application will compare the signal strength 