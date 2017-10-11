# To run this, you can install BeautifulSoup
# https://pypi.python.org/pypi/beautifulsoup4

# Or download the file
# http://www.py4e.com/code3/bs4.zip
# and unzip it in the same directory as this file

import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter URL:')
print(url)
count = input('Enter count:')
count = int(count)
position = input('Enter position:')
position = int(position)


for i in range(0, count+1):

    #read in url and soup it
    html = urllib.request.urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')

    if i < count:
        print ("Retrieving:", url)
    else:
        print ("Last Url: ", url)
        break

    # Retrieve all of the anchor tags
    tags = soup('a')

    # loop through tags and find the tag at position
    pos = 0
    for tag in tags:
        if pos == position-1:
            url = str(tag.get('href', None))
            break
        pos += 1