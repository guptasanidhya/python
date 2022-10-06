# import requests
# r=requests.get("https://financialmodelingprep.com/api/v3/profile/AAPL?apikey=6bcd8448d76bd341ffaf7d52f2208b90")
# print(r.text)
# print(r.status_code)
# url = "www.something.com"
# data = {
#     "p1":4,
#     "p2":8
# }
# r2 = requests.post(url=url, data=data)
# r=requests.get("https://google.com")
# print(r.text)


#How to make GET request through Python Requests
"""Python’s requests module provides in-built method called get()
 for making a GET request to a specified URI.
 requests.get(url, params={key: value}, args)
 """
#1
"""r = requests.get('https://api.github.com/users/naveenkrnl')

# check status code for response received
# success code - 200
print(r)

# print content of request
print(r.content)"""
#2

# import requests module
"""import requests

# Making a get request
response = requests.get('https://api.github.com/')

# print request object
print(response.url)

# print status code
print(response.status_code)
print(response.ok)
print(response.reason)
"""
#3
"""Response Methods
Method	Description
response.headers :	response.headers returns a dictionary of response headers.
response.encoding :	response.encoding returns the encoding used to decode response.content.
response.elapsed :	response.elapsed returns a timedelta object with the time elapsed from sending the request to the arrival of the response.
response.close() :	response.close() closes the connection to the server.
response.content :	response.content returns the content of the response, in bytes.
response.cookies :	response.cookies returns a CookieJar object with the cookies sent back from the server.
response.history :	response.history returns a list of response objects holding the history of request (url).
response.is_permanent_redirect :	response.is_permanent_redirect returns True if the response is the permanent redirected url, otherwise False.
response.is_redirect :	response.is_redirect returns True if the response was redirected, otherwise False.
response.iter_content() :	response.iter_content() iterates over the response.content.
response.json() :	response.json() returns a JSON object of the result (if the result was written in JSON format, if not it raises an error).
response.url :	response.url returns the URL of the response.
response.text :	response.text returns the content of the response, in unicode.
response.status_code :	response.status_code returns a number that indicates the status (200 is OK, 404 is Not Found).
response.request :	response.request returns the request object that requested this response.
response.reason :	response.reason returns a text corresponding to the status code.
response.raise_for_status() :	response.raise_for_status() returns an HTTPError object if an error has occurred during the process.
response.ok :	response.ok returns True if status_code is less than 200, otherwise False.
response.links :	 response.links returns the header links."""

#4
"""Authentication using Python Requests
Authentication refers to giving a user permissions to access a particular resource. 
Since, everyone can’t be allowed to access data from every URL, one would require authentication primarily.
To achieve this authentication,
typically one provides authentication data through Authorization
header or a custom header defined by server."""
# import requests module
"""import requests
from requests.auth import HTTPBasicAuth

# Making a get request
response = requests.get('https://api.github.com/ user, ',
			auth = HTTPBasicAuth('user', 'pass'))

# print request object
print(response)
"""
"""Replace “user” and “pass” with your username and password. 
It will authenticate the request and return a response 200 or else it will return error 403."""
#5
"""SSL Certificate Verification
Requests verifies SSL certificates for HTTPS requests, just like a web browser. 
SSL Certificates are small data files that digitally bind a cryptographic key to an organization’s
 details. Often, an website with a SSL certificate is termed as secure website. 
 By default, SSL verification is enabled, and Requests will throw a SSLError if it’s
  unable to verify the certificate.
"""
# import requests module
"""import requests

# Making a get request
response = requests.get('https://expired.badssl.com/')

# print request object
print(response)"""
"""This website doesn’t have SSL setup so it raises this error.
one can also pass the link to the certificate for validation via python requests only."""
# import requests module
"""import requests

# Making a get request
response = requests.get('https://github.com', verify ='/path/to/certfile')

# print request object
print(response)"""
"""This would work in case the path provided is correct for SSL certificate for github.com."""
#6
"""Session Objects
Session object allows one to persist certain parameters across requests. 
It also persists cookies across all requests made from the Session instance and will 
use urllib3’s connection pooling. So if several requests are being made to the same host, 
the underlying TCP connection will be reused, which can result in a significant performance increase. 
A session object all the methods as of requests.

Using Session Objects
Let us illustrate use of session objects by setting a cookie to a url and then making a request again 
to check if cookie is set."""
# import requests module
import requests

# create a session object
s = requests.Session()

# make a get request
s.get('https://httpbin.org/cookies/set/sessioncookie/123456789')

# again make a get request
r = s.get('https://httpbin.org/cookies')

# check if cookie is still set
print(r.text)

