import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

# Ingnore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input("Enter URL: ")
count = int(input("Enter count: "))
position = int(input("Enter position: "))

def scrapUrl (_url) :
    global url
    html = urllib.request.urlopen(_url, context=ctx).read()
    soup = BeautifulSoup(html, "html.parser")
    tags = soup("a")
    url = tags[position - 1].get("href", None)
    print("Retrieving:", url)
    return

try :
    print("Retrieving:", url)
    for i in range(count) :
       scrapUrl(url)
except :
    print("Something went wrong")