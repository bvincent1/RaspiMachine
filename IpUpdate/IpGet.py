import subprocess
import xml.etree.ElementTree as ET

from sys import argv

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

FILE_NAME = "IpAddr.xml"
FILE_LOCATION = "/home/stjoes/Dropbox/Misc/scripts/PortChange/"

def getIpAddress(target_string = ""):
	if target_string == '':
		target_string = "inet addr"
	out = subprocess.check_output(["ifconfig"]).decode("utf-8")
	target_index = out.find(target_string)
	return out[target_index + len(target_string) + 1:target_index + len(target_string) + 14]

# return either true (same ip as last time) or false (new ip addr)
# takes the full 13 length ip addr
def checkIpAddr(ip_addr):
	try:
		tree = ET.parse(FILE_LOCATION+FILE_NAME)
		root = tree.getroot()
	except:
		root = ET.Element('data')

	addr_list = root.findall('address')

	if len(addr_list) < 1:
		addr = ET.SubElement(root, 'address')
		addr.set('value', ip_addr)

		tree = ET.ElementTree(root)
		tree.write(FILE_LOCATION+FILE_NAME)

		return False

	elif len(addr_list) > 0:
		if addr_list[-1].get('value') == ip_addr:
			return True
		else:
			addr = ET.SubElement(root, 'address')
			addr.set('value', ip_addr)

			tree = ET.ElementTree(root)
			tree.write(FILE_LOCATION+FILE_NAME)

			return False

if __name__ == '__main__':
	addr = getIpAddress()
	print(addr)

