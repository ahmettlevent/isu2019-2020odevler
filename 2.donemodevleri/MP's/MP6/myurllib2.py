import ssl
import urllib.request as urllib2


def urlopen(url):
    gcontext = ssl.SSLContext()
    c = urllib2.urlopen(url, context=gcontext)
    return c
