# Superfox # WIll avaliable soon on pypi.org

Send web requests with superfox. Check example codes for more information about usage.

# Superfox Usage 

While send request you may use http or https. Without it superfox also will send request. You are free to use it.

### [get] Module
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
Avaliable :

url
text
ip
domain
status_code
response_time
headers
"""
```


### [post] Module

Explaination of this sample code : 
This code will post a payload to this url.

```python 
import superfox as fox # import module 

# Payload -->
data = {
    'name' : 'error',
    'projectname' : 'firefox',
    'post' : True # bla bla
}

url = 'url adress to post'
req = fox.post(url,payload=data) # send request. 

print(req.text)  

"""
Avaliable :

url
text
ip
domain
status_code
headers
"""
```

## Response Time
```python 
import superfox as fox

req = fox.get("google.com")
print(req.response_time)
```
>>>>>>> e36f084454b643ded583777af0f1a3eb129375b2
