#!/usr/bin/env python
# Requests library is not standard with some distributions and
# may require extra install.

# This Script uses Python3

# OS X links Python3 to an older version of OpenSSL. In order to 
# resolve this issue you can install pyopenssl idna.
# (e.g., pip3 install pyopenssl idna)

# Library imports and code referenced orignally from https://github.com/p0lr/pan_dhcp
# Check @p0lr for more info.

import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
import xml.etree.ElementTree as ET


# system variable represents device being queried. This can be in the form
# of an IP address or FQDN (e.g., 10.10.10.1 or system.example.com).
# 
# Change to your system. 
system = "please put a system name or IP here"

# api_key variable represents the key needed to access the system. To generate
# an API Key manually refer to 
# https://www.paloaltonetworks.com/documentation/71/pan-os/xml-api/get-started-with-the-pan-os-xml-api/get-your-api-key
# Check https://live.paloaltonetworks.com/t5/Management-Articles/Getting-Started-with-the-API/ta-p/65889
# for getting started with PAN-Python.
#
# To reset an api key simply change the account password that generated the key 
# (e.g., if admin generated the key, simply reset the password)
#
# Change to your API Key 
api_key = "<please gen an API Key"

#Make call to the system to get XML NAT IPPOOL lease information
natpool = 'https://' + system + '/api?type=op&cmd=<show><running><ippool></ippool></running></show>&key=' + api_key
r = requests.get(natpool, verify=False)

# Testing for correct response
# print(r)

tree = ET.fromstring(r.text)

print(r.content)