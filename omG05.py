def atequiz(randmlimit=7,trynum=5):
    """ ちょっと拡張してみた   """
    # 最初に考えた数字宛クイズ
    import random
    print('{0}回のうちに1から{0}までの数字を当ててください\n {1}回までリトライできます。'.format(randmlimit,trynum))
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


# 入力は randmlimit > trynumでないと意味がない
atequiz(5,2)




