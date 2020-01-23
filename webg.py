import requests
res = requests.get('http://google.com/')
# print(res.text)
with open('getweb.html','w') as f:
    f.write(res.text)