# fileを読み込んで文字列検索する
# とりあえずtakaraがいくつあるかを読み込む
# with を使ってcloseをなくした withを使うと例外が起きてもcloseしてくれる
# もうちょっとスマートな方法でやってみる　countを使う
# takaraはomankoに置換（ちかん）
# 複数のPCで行う場合というより、VScodeとgit bashでやる場合にもAuthorの変更をすれば再度PULLが必要
# でも、これでmergeの仕方もわかった。どこが競合するかも表示してくれることがわかった。
# ファイル書き出しには write()が必要。これがないとstringバッファ書き込まれてるだけになってしまう。
# 今回は文字列とリストの違いを知ることになった。文字列は変更できない。リストはあとから変更できる。

with open('txtfile.txt','r') as f :
    with open('otextfile.txt','w') as of:
        count = 0
        ocount = 0
        i_st = f.read()
        count = i_st.count('takara')
        o_st = i_st.replace('takara','omanko')
        of.write(o_st)
        ocount = o_st.count('omanko')
        print(o_st)


print('txtfile.txtの中のtakaraの数は',count)
print('otextfile.txtの中のomankoの数は',ocount)


