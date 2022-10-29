# Superagent LIB
from superfox.con import *
# Other
from urllib.request import urlopen
import socket 



class get:
    url = ''
    text = ''
    ip = ''
    domain = ''
    status_code = 0
    response_time = 0
    headers = ''
    
    def __init__(agent,url):
        if(url.startswith('http') and ('://' in url)):
            get.url = url
            get.domain = getdomain(url)
        else:
            get.url = gethttp(url)+url
            get.domain = getdomain(url)
        
        get.response_time = getrt(get.url)
        try:
            sr = urlopen(get.url)
            
            get.text = sr.read()
            get.status_code = sr.getcode()
            get.headers = sr.info()
        except:
            pass # An error occured
            
        get.ip = socket.gethostbyname(get.domain)