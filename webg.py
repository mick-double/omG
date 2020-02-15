# error 処理を入れる

import requests,bs4,csv,pprint,json

output00 = 'getweb.html'
output01 = 'get_select.html'
soure_html = 'http://weather.livedoor.com/forecast/webservice/json/v1?city=120010'

res = requests.get(soure_html)
pprint.pprint(res.json())

if res.status_code != 200 :
    res.raise_for_status()
    print(res.status_code)

soup = bs4.BeautifulSoup(res.text,"html.parser")
print(soup.title)

# htmlを整形してくれるもの
# print(soup.prettify())
elems = soup.select('#inner-contents a')

with open(output00,'w') as f:
    print('正常に読まれてgetweb.htmlファイに書き込みます！')
    str_0 = json.dumps(res.json())
    f.write(str_0)

with open(output01,'w') as fs:
    print('selectされた内容を抽出')
    for elem in elems:
        print(elem.getText(),elem.get('href'))
        fs.write(elem.getText())
        fs.write(elem.get('href'))

# 文字列操作
with open(output01,'r') as f01:
    reader = f01.readlines()
    reader[0]=reader[0].strip('\t')
    for line in range(len(reader)):
        print(reader[0])
