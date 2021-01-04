#!/usr/bin/env python

import subprocess
import optparse
import re

def get_arguments():
    parser = optparse.OptionParser()
    parser.add_option("-i", "--interface", dest="interface", help="Interface to change mac address")
    parser.add_option("-m", "--mac", dest="mac_address", help="Address to change mac address")
    (options, arguments) = parser.parse_args()
    if not options.interface:
        parser.error("[-] Please enter the interface. Use --help to get help")

    elif not options.mac_address:
        parser.error("[-] Please enter the mac address. Use --help to get help")

    return options

def mac_changer(interface, mac_address):
    subprocess.call(["ifconfig", interface, "down"])
    subprocess.call(["ifconfig", interface, "hw", "ether", mac_address])
    subprocess.call(["ifconfig", interface, "up"])


options = get_arguments()
# mac_changer(options.interface, options.mac_address)

ifconfig_result = subprocess.check_output(["ifconfig", options.interface])
print(ifconfig_result)

search_value = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w", ifconfig_result)
if search_value:
    print(search_value.group(0))
else:
    print("[-] Could not read mac address")

