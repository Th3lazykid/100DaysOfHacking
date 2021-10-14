"Not a shred of evidence exists in favor of the idea that life is serious." - Brendan Gill

# Day-16 Summary:

### Things Done Today: 

- Pretyy busy day with college stuff, and since really hooked to SSRF Port-Swigger labs, gonna complete these labs and will then continue with the wreath network. 

- [X] **SSRF Lab #3:** [Web-Security Academy - SSRF with blacklist-based input filter](https://portswigger.net/web-security/ssrf/lab-ssrf-with-blacklist-filter) -- PortSwigger; [Rana Khalil's Course](https://ranakhalil.teachable.com/);

  - Goal: Change the stock check URL to access the admin interface at http://localhost/admin and delete the user carlos. 
  - Condition: The developer has deployed two weak anti-SSRF defenses that you will need to bypass. 
  - Solution: So in order to access the localhost, we need bypass 2 weeknessess. `127.0.0.1` is blacklisted. Using `127.1`, gives the access to the localhost. And in order to access the admin page, gotta encode the character a in admin twice, because:
    - It uses regex to blacklist words
    - Url decoding once
      - hence the payload: http://127.1/%25%36%31dmin
      - payload to delete the user carlos: http://127.1/%25%36%31dmin/delete?username=carlos

  - Automation: Find the python code [HERE](/Python/SSRF-lab3.py). Not explaining because it is the same script as lab-1, just payload diff. So check out the explanation [here](/Days/Day14.md).

