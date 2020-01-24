# fileを読み込んで文字列検索する
# とりあえずtakaraがいくつあるかを読み込む
# with を使ってcloseをなくした withを使うと例外が起きてもcloseしてくれる
# もうちょっとスマートな方法でやってみる　countを使う
# takaraはomankoに置換（ちかん）

with open('txtfile.txt','r') as f :
    with open('otextfile.txt','w') as of:
        count = 0
        ocount = 0
        l = f.read()
        count = l.count('takara')
        of = l.replace('takara','omanko')
        ocount = of.count('omanko')
        print(of)


print('txtfile.txtの中のtakaraの数は',count)
print('otextfile.txtの中のomankoの数は',ocount)
