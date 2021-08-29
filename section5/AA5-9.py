import sys
from collections import deque
#sys.stdin=open("input.txt", "r")
a = input()
b = input()

ad = dict()
bd = dict()

for i in a:
    if i in ad.keys():
        ad[i]+=1
    else:
        ad[i]=1

for i in b:
    if i in bd.keys():
        bd[i]+=1
    else:
        bd[i]=1

if ad==bd:
    print('YES')
else:
    print('NO')
    




        


