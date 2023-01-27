import subprocess
import time
from utility.fetch_data import fetch_var


def check_wifi_connection_mac():
    # Check available connections
    available_its = []
    devices = subprocess.check_output(
        ["/System/Library/PrivateFrameworks/Apple80211.framework/Versions/Current/Resources/airport", '-s'])
    devices = devices.decode('ascii')
    devices = devices.split("\n")
    for _ in devices:
        if (_.find("ITS") != -1):
            available_its.append(_.replace(" ", ""))
        # print(available_its)
    #filtering data
    only_its = []
    its = []
    for _ in available_its:
        its = _.split("-")
        if its[0] not in only_its:
            only_its.append(its[0])

    # Printing availble SSID's
    # print("Available SSID'S: ")
    # for _ in only_its:
    #     print(_)
    if only_its == []:
        print("No ITS SSID's Found")
        print("Rechecking in 5 secs")
        time.sleep(5)
        check_wifi_connection_mac()
    else:
        # Fetching SSID from the var file
        if len(only_its) >= 1:
            network_to_connect = only_its[0]
        # Get preferred network from the var file
        preferred_network = fetch_var("Preferred network")
        # print("preferred network : ", preferred_network )
        if preferred_network in only_its:
            network_to_connect = preferred_network

        # Connect to the network {networksetup -setairportnetwork en0 <SSID_OF_NETWORK> <PASSWORD>}
        # only_its in not empty
        # check if the network is already connected to the prefered network
        network_connected = subprocess.check_output(
            ["/System/Library/PrivateFrameworks/Apple80211.framework/Versions/Current/Resources/airport", "-I", "|", "awk", "'/", "SSID:/", "{print $2}'"])
        network_connected = network_connected.decode('ascii')
        network_connected = network_connected.split("\n")
        for _ in network_connected:
            if (_.find("ITS") != -1):
                network_connected = _.replace(" ", "")
        # print(network_connected)
        # if len(network_connected) >= 1:
        #     for i in network_connected:
        #         network_connected.append(i.split(':'))
        # print(network_connected)
        if preferred_network in network_connected:
            # print("Already connected to the preferred network: {}".format(
            #     network_connected[1]))
            pass
        else:
            if len(only_its) != 0:
                subprocess.check_output(
                    ['networksetup', '-setairportnetwork', 'en0', network_to_connect, 'iiitbbsr'])
                # print("Connected to : {} ".format(network_to_connect))
            else:
                print("No ITS SSID's found")
                print("Rechecking in 5 secs")
                time.sleep(5)
                check_wifi_connection_mac()

def check_wifi_connection_linux():
    # Check available connections
    available_its = []
    # devices = subprocess.check_output(
    #     ["nmcli", "dev", "wifi"])
    devices = subprocess.check_output(["iwlist", "scan"])
    devices = devices.decode('ascii')
    devices = devices.split("\n")
    for _ in devices:
        if (_.find("ITS") != -1):
            available_its.append(_.replace(" ", ""))
        # print(available_its)
    #filtering data
    only_its = []
    its = []
    for _ in available_its:
        its = _.split("-")
        if its[0] not in only_its:
            only_its.append(its[0])

    # Printing availble SSID's
    # print("Available SSID'S: ")
    # for _ in only_its:
    #     print(_)
    if only_its == []:
        print("No ITS SSID's Found")
        print("Rechecking in 5 secs")
        time.sleep(5)
        check_wifi_connection_linux()
    else:
        # Fetching SSID from the var file
        if len(only_its) >= 1:
            network_to_connect = only_its[0]
        # Get preferred network from the var file
        preferred_network = fetch_var("Preferred network")
        # print("preferred network : ", preferred_network )
        if preferred_network in only_its:
            network_to_connect = preferred_network

        # Connect to the network {networksetup -setairportnetwork en0 <SSID_OF_NETWORK> <PASSWORD>}
        # only_its in not empty
        # check if the network is already connected to the prefered network
        # network_connected = subprocess.check_output(
        #     ["nmcli", "dev", "wifi"])
        network_connected = subprocess.check_output(["iwlist", "scan"])
        network_connected = network_connected.decode('ascii')
        network_connected = network_connected.split("\n")
        for _ in network_connected:
            if (_.find("ITS") != -1):
                network_connected = _.replace(" ", "")
        # print(network_connected)
        # if len(network_connected) >= 1:
        #     for i in network_connected:
        #         network_connected.append(i.split(':'))
        # print(network_connected)
        if preferred_network in network_connected:
            # print("Already connected to the preferred network: {}".format(
            #     network_connected[1]))
            pass
        else:
            if len(only_its) != 0:
                subprocess.check_output(
                    ['nmcli', 'dev', 'wifi', 'connect', network_to_connect, 'password', 'iiitbbsr'])
                # print("Connected to : {} ".format(network_to_connect))
            else:
                print("No ITS SSID's found")
                print("Rechecking in 5 secs")
                time.sleep(5)
                check_wifi_connection_linux()

def check_wifi_connection_win():
    # Check available connections
    available_its = []
    devices = subprocess.check_output(
        ["netsh", "wlan", "show", "networks"])
    devices = devices.decode('ascii')
    devices = devices.split("\n")
    for _ in devices:
        if (_.find("ITS") != -1):
            available_its.append(_.replace(" ", ""))
        # print(available_its)
    #filtering data
    only_its = []
    its = []
    for _ in available_its:
        its = _.split("-")
        if its[0] not in only_its:
            only_its.append(its[0])

    # Printing availble SSID's
    # print("Available SSID'S: ")
    # for _ in only_its:
    #     print(_)
    if only_its == []:
        print("No ITS SSID's Found")
        print("Rechecking in 5 secs")
        time.sleep(5)
        check_wifi_connection_win()
    else:
        # Fetching SSID from the var file
        if len(only_its) >= 1:
            network_to_connect = only_its[0]
        # Get preferred network from the var file
        preferred_network = fetch_var("Preferred network")
        # print("preferred network : ", preferred_network )
        if preferred_network in only_its:
            network_to_connect = preferred_network

        # Connect to the network {networksetup -setairportnetwork en0 <SSID_OF_NETWORK> <PASSWORD>}
        # only_its in not empty
        # check if the network is already connected to the prefered network
        network_connected = subprocess.check_output(
            ["netsh", "wlan", "show", "networks"])
        network_connected = network_connected.decode('ascii')
        network_connected = network_connected.split("\n")
        for _ in network_connected:
            if (_.find("ITS") != -1):
                network_connected = _.replace(" ", "")
        # print(network_connected)
        # if len(network_connected) >= 1:
        #     for i in network_connected:
        #         network_connected.append(i.split(':'))
        # print(network_connected)
        if preferred_network in network_connected:
            # print("Already connected to the preferred network: {}".format(
            #     network_connected[1]))
            pass
        else:
            if len(only_its) != 0:
                subprocess.check_output(
                    ['netsh', 'wlan', 'connect', 'name=', network_to_connect, 'ssid=', network_to_connect, 'interface=Wi-Fi'])
                # print("Connected to : {} ".format(network_to_connect))
            else:
                print("No ITS SSID's found")
                print("Rechecking in 5 secs")
                time.sleep(5)
                check_wifi_connection_win()