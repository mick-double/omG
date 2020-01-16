# 最初に考えた数字宛クイズ
import random
print('5回のうちに1から6までの数字を当ててください')
answer = random.randint(1,7)
inputnum = []
for i in range(5) :
    inputnum.append(int(input()))
    if inputnum[i] == answer :
        print('やった！正解です')
        print()
        break
    elif i < 4:
        print('もう一回')
    else:
        print('残念でした')
print()
print('正解は',answer)
print('打ち込み履歴は')
print(inputnum)
