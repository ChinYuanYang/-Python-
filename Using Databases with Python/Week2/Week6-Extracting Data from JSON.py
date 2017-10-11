import urllib.request, urllib.parse, urllib.error
import json

url = ('http://py4e-data.dr-chuck.net/comments_5136.json')
html = urllib.request.urlopen(url).read().decode()
json_code = json.loads(html)

json_deep = json_code['comments']

list_test = []
for count in json_deep:
    countnumber = count['count']
    list_test.append(countnumber)
print (sum(list_test))