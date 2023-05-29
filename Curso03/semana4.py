# print(ord("H"))
# print(ord("e"))
# print(ord("\n"))

import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup

# fileHandler = urllib.request.urlopen("http://data.pr4e.org/romeo.txt")
# for line in fileHandler :
#     print(line.decode().strip())

url = input("Enter - ")
html = urllib.request.urlopen(url).read()
soup = BeautifulSoup(html, "html.parser")
print(soup)

# Retrieve all of the anchor tags
# tags = soup("a") # shorcut for soup.find_all("a")
tags = soup("a")
print(tags)
print(type(tags))
for tag in tags :
    print(tag.get("href", None))