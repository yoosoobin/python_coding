
import sys
import collections
#sys.stdin = open('input.txt','rt')


def prize(x):
    if  x[0] == x[1] and x[1] == x[2] and x[0] == x[2]:
        return 10000+x[0]*1000
    elif x[0] != x[1] and x[1] != x[2] and x[0] != x[2]:
        m = max(x)
        return m*100
    else:
        dict = collections.Counter(x)
        return dict.most_common(1)[0][0] *100 + 1000


n = int(input())
dice_list=[]
prize_list=[]

for i in range(n):
    dice_list.append(list(map(int,input().split())))

for i in dice_list:
    prize_list.append(prize(i))

print(max(prize_list))









    



