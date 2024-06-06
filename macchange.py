#!/usr/bin/python

import subprocess
from termcolor import colored

def change_mac_address(interface, mac):
	subprocess.call(["ifconfig",interface,"down"]) #this executes the command in the brackets and makes the interface down
	subprocess.call(["ifconfig",interface,"hw","ether",mac]) #for example ifconfig eth0 hw ether aa:bb:cc:dd:ee:ff
	subprocess.call(["ifconfig",interface,"up"]) #makes interface up



def main():
	interface = input("[+] Enter interface To Change Mac Address On: ")
	new_mac_address = input("[+] Enter Mac Address To Change To: ")

	#check the output of the ifconfig command
	before_change = subprocess.check_output(["ifconfig",interface])
	change_mac_address(interface,new_mac_address)
	after_change = subprocess.check_output(["ifconfig",interface])

	if before_change == after_change:
		print(colored("[!] Failed to change Mac Address to: "+new_mac_address, "red"))
	else:
		print(colored("[*] Mac Address changed to: "+new_mac_address+" on interface: "+interface, "green"))


main()