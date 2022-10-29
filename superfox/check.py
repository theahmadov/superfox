from urllib.request import urlopen

def getdomain(url):
    if(url[len(url)-1]=='/'):
        url = url[:-1]
    else:
        pass

    if(url.startswith('http://')):
        url = url.split('http://')[1]
    elif(url.startswith('https://')):
        url = url.split('https://')[1]

    return url.split('/')[0]

def gethttp(domain):
    try:
        urlopen('https://'+domain).read()
    except:
        return 'http://'

    return 'https://'

# *
# * Tests
# *

#print(getdomain('https://test.test/'))