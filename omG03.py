# 最初に考えた数字当てクイズ
import random
print('5回のうちに1から6までの数字を当ててください')
print('   ',end='')
answer = random.randint(1,7)
inputnum = []
for i in range(5) :
    inputnum.append(int(input()))
    if inputnum[i] == answer :
        print('やった！正解です')
        print('   ',end='')
        break
    elif i < 4:
        print('もう一回')
        print('   ',end='')
    else:
        print('残念でした')
        print('   ',end='')
print()
print('正解は',answer)
print('打ち込み履歴は')
print('   ',end='')
print(inputnum)
