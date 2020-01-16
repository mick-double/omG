# 最初に考えた数字宛クイズ
import random
print('5回のうちに1から6までの数字を当ててください')
answer = random.randint(1,7)
inputnum = []
for i in range(5) :
    print('入力してください: ',end='')
    inputnum.append(int(input()))
#    inputnum.append(int(input()))
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
