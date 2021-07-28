#!/usr/bin/env python


import optparse
import re
import subprocess

def get_arguments():
    parser = optparse.OptionParser()
    parser.add_option("-i", "--interface", dest="interface", help="Set the interface")
    parser.add_option("-m", "--mac", dest="mac", help="Enter the new mac_address")
    (options, arguments) = parser.parse_args()
    if not options.interface:
        parser.error("set the interface , use -help for more info")
    elif not options.mac:
        parser.error("enter the mac ,use -help for more info")
    return options

def mac_changer(interface, mac):
    print(f"mac address changing to {mac}")
    subprocess.call(["ifconfig", interface, "down"])
    subprocess.call(["ifconfig", interface, "hw", "ether", mac])
    subprocess.call(["ifconfig", interface, "up"])
def current_mac(interface):
    ifconfig_output = subprocess.check_output(["ifconfig", interface])
    ether_output = re.search("\w\w:\w\w:\w\w:\w\w:\w\w:\w\w", str(ifconfig_output))
    if ether_output:
        return ether_output.group(0)
    else:
        print("cannot read the mac address")


options = get_arguments()
inter = options.interface
m = options.mac
currentMac = current_mac(inter)
print("current Mac Adrress = " + str(currentMac))
mac_changer(inter, m)
currentMac = current_mac(inter)
if currentMac==m:
    print("succesfully changed to=" + currentMac)
else:
    print("error occured")
