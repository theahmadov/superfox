# Superfox # WIll avaliable soon on pypi.org

Send web requests with superfox. Check example codes for more information about usage.

# Superfox Usage

While send request you may use http or https. Without it superfox also will send request. You are free to use it.
```python 
import superfox as fox # import module 

req = fox.get("google.com") # Send request 

print(req.text)     # HTML Text of page
print(req.ip)       # IP adress of website
print(req.domain)   # Domain Adress
print(req.status_code)   # Website Status Code
# . 
# .
# .

"""
url
text
ip
domain
status_code
response_time
headers
"""
```

# Example 

## Headers

```python 
import superfox as fox

req = fox.get("google.com")
print(req.headers)
```

## Response Time
```python 
import superfox as fox

req = fox.get("google.com")
print(req.response_time)
```
