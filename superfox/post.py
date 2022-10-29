# Superagent LIB
from superfox.con import *
# Other
from urllib import request, parse
import socket 



class post:
    url = ''
    text = ''
    ip = ''
    domain = ''
    status_code = 0
    headers = ''
    
    def __init__(agent,url,payload):
        if(url.startswith('http') and ('://' in url)):
            post.url = url
            post.domain = getdomain(url)
        else:
            post.url = gethttp(url)+url
            post.domain = getdomain(url)

        payload = parse.urlencode(payload).encode()
        req =  request.Request(post.url, data=payload)
        rget = request.urlopen(req)

        post.text = rget.read()
        post.status_code = rget.getcode()
        post.headers = rget.info()
        post.ip = socket.gethostbyname(post.domain)