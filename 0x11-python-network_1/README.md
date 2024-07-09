0x11. Python - Network #1
0-hbtn_status.py:  Python script that fetches https://alx-intranet.hbtn.io/status
1-hbtn_header.py: Python script that takes in a URL, sends a request to the URL and displays the value of the X-Request-Id variable found in the header of the response.
2-post_email.py: Python script that takes in a URL and an email, sends a POST request to the passed URL with the email as a parameter, and displays the body of the response (decoded in utf-8)
Python script that takes in a URL, sends a request to the URL and displays the body of the response (decoded in utf-8).
4-hbtn_status.py
Write a Python script that fetches https://alx-intranet.hbtn.io/status

You must use the package requests
You are not allow to import packages other than requests
The body of the response must be display like the following example (tabulation before -)

5-hbtn_header.py:
Write a Python script that takes in a URL, sends a request to the URL and displays the value of the variable X-Request-Id in the response header

You must use the packages requests and sys
You are not allow to import other packages than requests and sys
The value of this variable is different for each request
You don’t need to check script arguments (number and type)

6-post_email.py:
Write a Python script that takes in a URL and an email address, sends a POST request to the passed URL with the email as a parameter, and finally displays the body of the response.

The email must be sent in the variable email
You must use the packages requests and sys
You are not allowed to import packages other than requests and sys
You don’t need to error check arguments passed to the script (number or type)
Please test your script in the sandbox provided, using the web server running on port 5000

7-error_code.py:
Write a Python script that takes in a URL, sends a request to the URL and displays the body of the response.

If the HTTP status code is greater than or equal to 400, print: Error code: followed by the value of the HTTP status code
You must use the packages requests and sys
You are not allowed to import packages other than requests and sys
You don’t need to check arguments passed to the script (number or type)

