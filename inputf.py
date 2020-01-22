# fileを読み込んで文字列検索する
# とりあえずtakaraがいくつあるかを読み込む

f = open('txtfile.txt','r')

# ファイルの内容表示
# print(f.read())

# リストに読み込む

l = f.readlines()

# fileの長さを表示
print('行数は',len(l))

count = 0
for n in range(len(l)):
    print(l[n].strip())
    if  'takara' in l[n]:
        count = count + 1

print('takaraの数は',count)

f.close()
