import re
import platform
import subprocess
import optparse


def change_mac(interface, new_mac):
    print("[+] Changing Mac Address for " + interface + " to " + new_mac)
    subprocess.call(["ifconfig", interface, "down"])
    subprocess.call(["ifconfig", interface, "hw","ether",new_mac])
    subprocess.call(["ifconfig", interface, "up"])

def fetchArgs():
    parser = optparse.OptionParser()
    parser.add_option("-i","--interface", dest="interface", help="Interface to change MAC Address")
    parser.add_option("-m","--mac",dest ="new_address", help = "New MAC address")
    (options, arguments) = parser.parse_args()
    if not options.interface:
        parser.error("[+] Please specify an interface, use --help for more info.")
    elif not options.new_address:
        parser.error("[+] Please specify a new mac, use --help for more info.")
    
    return options
    
def DeviceMac(interface):
    ifconfigFetch = subprocess.check_output(["ifconfig", interface])
    currentMac = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w", str(ifconfigFetch))
    if currentMac:
        return currentMac.group(0)
    else:
        print("[+] Couldnt read MAC.")

OperatingSystem = platform.system()
options = fetchArgs()
currentMac = DeviceMac(options.interface)
print("> Current MAC:" + currentMac)
print("> OS: " + OperatingSystem)
change_mac(options.interface, options.new_address)
newMac = DeviceMac(options.interface)

if newMac == options.new_address:
	print("[+] MAC Address changed.\n> New MAC: "+newMac)
else:
	print("[-] Error occured while changing MAC.")
