# Superagent LIB
from superfox.check import *
# Other
from urllib.request import urlopen
import socket 



class get:
    url = ''
    text = ''
    ip = ''
    domain = ''

    def __init__(agent,url):
        agent.url = url
        get.url = gethttp(url)+url
        get.domain = getdomain(url)
        #
        # Gathered informations.
        #
        
        try:
            get.text = urlopen(url).read()
        except:
            try:
                get.text = urlopen(get.url).read()
            except:
                pass

        get.ip = socket.gethostbyname(get.domain)