from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl
import xml.etree.ElementTree as ET

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter location: ')
print("Retrieving", url)
html = urlopen(url, context=ctx).read()
print("Retrieved", len(html), "characters")

xmlData = ET.fromstring(html)
countInComments = xmlData.findall(".//count")#https://docs.python.org/3/library/xml.etree.elementtree.html#supported-xpath-syntax
print("Count", len(countInComments))
countValues = []
for count in countInComments:
    countValues.append(int(count.text))
print("Sum", sum(countValues))