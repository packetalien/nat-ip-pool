#!/usr/bin/env python
# ========================================================================
# THE SOFTWARE IS PROVIDED "AS IS" AND THE AUTHOR DISCLAIMS ALL WARRANTIES
# WITH REGARD TO THIS SOFTWARE INCLUDING ALL IMPLIED WARRANTIES OF
# MERCHANTABILITY AND FITNESS. IN NO EVENT SHALL THE AUTHOR BE LIABLE FOR
# ANY SPECIAL, DIRECT, INDIRECT, OR CONSEQUENTIAL DAMAGES OR ANY DAMAGES
# WHATSOEVER RESULTING FROM LOSS OF USE, DATA OR PROFITS, WHETHER IN AN
# ACTION OF CONTRACT, NEGLIGENCE OR OTHER TORTIOUS ACTION, ARISING OUT OF
# OR IN CONNECTION WITH THE USE OR PERFORMANCE OF THIS SOFTWARE.
# ========================================================================
# Requests library is not standard and
# may require extra install.
# Run the following at a command prompt (linux/macOS)
# ========================================================================
# pip install requests
# ========================================================================
# TODO
# - Add command line args and user input
# - Add input validation
# - Add string output formatting


import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
import xml.etree.ElementTree as ET


# system variable represents device being queried. This can be in the form
# of an IP address or FQDN (e.g., 10.10.10.1 or system.example.com).
# 
# Change to your system.

fwip = 'pacha.local'
username = 'admin'
password = 'paloalto'




# getkey function adapted/copied from @p0lr.

keycall = "https://%s/api/?type=keygen&user=%s&password=%s" % (fwip,username,password)

def getkey():
    try:
        r = requests.get(keycall, verify=False)
        tree = ET.fromstring(r.text)
        if tree.get('status') == "success":
            apikey = tree[0][0].text
    except requests.exceptions.ConnectionError as e:
        print("There was a problem connecting to the firewall.  Please check the connection information and try again.")
    
    return apikey

def getnatpool(passkey):
    try:
        type = "op"
        cmd = "<show><running><ippool></ippool></running></show>"
        call = "https://%s/api/?type=%s&cmd=%s&key=%s" % (fwip, type, cmd, passkey)
        r = requests.get(call, verify=False)
        # response is single element, needs formatting
        #tree = ET.fromstring(r.text)
        return r.text
    except requests.exceptions.ConnectionError as e:
        print("There was a problem in getting natpool stats. \n Please vent frustrations in a safe manner and throw a candy bar at the wall! \n If this is helpful the error was captured as: " + e)

def main():
    try:
        mainkey = getkey()
        results = getnatpool(mainkey)
        print(results)
    except:
        print("Something happened and your output didn't.")


if __name__ == "__main__":
    main()
