import urllib.request

url = 'http://weather.livedoor.com/'

data = urllib.request.urlopen(url)
html = data.read()
print(html)
data.close()
# urllib.request.urlretrieve(url,'./10.gif')