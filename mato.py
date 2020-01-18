# 最初に考えた数字当てクイズ
# ダブルチャンスがある抽選　n個の数からいくつ当たるか
# ダブルチャンスへ入力した数値がそのまま使われる

import random

def atequiz(randmlimit=7,trynum=5):
    """ ちょっと拡張してみた 関数にしていくつでもできるように拡張  

    返値はインプットの文字列

    """

    print("""{0}回のうちに1から{0}までの数字を当ててください 
    {1}回までリトライできます。""".format(randmlimit,trynum))
    answer = random.randint(1,randmlimit)
    inputnum = []
    for i in range(trynum) :
        print('入力してください: ',end='')
        inputnum.append(int(input()))
        if inputnum[i] == answer :
            print('\n\n\nおめでとうございます。正解です')
            print()
            break
        elif i < 4:
            print('\n残念。もう一回!!')
        else:
            print('\n\n残念ながら不正解でした')
    print('正解は',answer,'でした')
    print()
    print('打ち込み履歴は',inputnum,'でした')
    print('\n{:^30}'.format('お疲れ様でした\n\n'))
    return inputnum


def saichusen(limit=10):
    """ ダブル抽選会 """
    print('あなたの選んだ',inputnum,'を再抽選します')
    print('何個の抽選にしますか？3個以内にしてください')
    dinputnum = int(input())
    print('入力=',dinputnum)
    
    base = list(range(1,limit))
    danswer = random.sample(base,dinputnum)

    # 見栄えが悪いので昇順でソートする。
    # 関数そのものを動かさないとdanswerに入ってくれない
    danswer.sort()

    print('再抽選結果は',danswer,'でした')
    
    # 集合(set)を使うと重複しているものを取り出せる
    # ここでは積集合を使う(interseciton)
    # 集合にするためにはset()を使う
    sdanswer = set(danswer)
    sinputnum = set(inputnum)
    atari = sdanswer.intersection(sinputnum)
    
    if len(atari) == 0:
        print('残念でした。再抽選は当たりませんでした。')
    else:
        print('おめでとうございます。再抽選で{0}個当たりました'.format(len(atari)))
        print('当たったのは',atari,'です')
    



    
# 入力は randmlimit > trynumでないと意味がない
# まずは数当てゲーム
inputnum = atequiz(10,2)

# debug 用
# import pdb; pdb.set_trace()

# 入力した値を使って再抽選する
# inputnumは外で使うとそのまま次の関数でも生きるのか
# グローバル変数になってしまっている

saichusen()

    












