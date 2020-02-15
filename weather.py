# error 処理を入れる

import requests,bs4,csv,pprint,json

output00 = 'getweb.html'
output01 = 'get_select.html'
output01_json = 'getweb.json'
output02_json = 'ichikawa.json'
soure_html = 'http://weather.livedoor.com/forecast/webservice/json/v1?city=120010'
second_html = 'http://weather.livedoor.com/forecast/webservice/json/v1?city=1220300'


res = requests.get(soure_html)
pprint.pprint(res.json())
json_data = res.json()

if res.status_code != 200 :
    res.raise_for_status()
    print(res.status_code)


# htmlを整形してくれるもの
# print(soup.prettify())

with open(output01_json,'w') as f:
    print('正常に読まれてgetweb.jsonファイに書き込みます！')
    # str_0 = json.dumps(pprint.pprint(res.json()))
    json.dump(json_data,f,indent=4,ensure_ascii=False)

# resオブジェクトが辞書型なので要素を指定して千葉県を表示する

print(json_data['description']['publicTime'],'の情報です。\n','千葉県の明日の天気は',json_data['description']['text'])

# ichikawa city no tenki


res_ichikawa = requests.get(second_html)

soup = bs4.BeautifulSoup(res_ichikawa.text,"html.parser")
print(soup.prettify())
print(soup.title)

# elems = soup.select('#inner-contents a')


json_ichikawa = res_ichikawa.json()
#    with open(output02_json,'w') as f:
#        print('正常に読まれてichikawa.jsonファイに書き込みます！')
#        # str_0 = json.dumps(pprint.pprint(res.json()))
#        json.dump(json_data,f,indent=4,ensure_ascii=False)


