# fileを読み込んで文字列検索する
# とりあえずtakaraがいくつあるかを読み込む
# with を使ってcloseをなくした withを使うと例外が起きてもcloseしてくれる

with open('txtfile.txt','r') as f :
    l = f.readlines()

    # fileの長さを表示
    print('行数は',len(l))

    count = 0
    for n in range(len(l)):
        print(l[n].strip())
        if  'takara' in l[n]:
            count = count + 1

    print('takaraの数は',count)



