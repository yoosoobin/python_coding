import sys
from collections import deque
#sys.stdin=open("input.txt", "r")
es = input()
n = int(input())
order = [input() for _ in range(n)]
ess=[]
for i in es:
    ess.append(i)



for n,i in enumerate(order):
    i = list(i)
    i = deque(i)
    for j in list(i):
        if j in ess:
            i.append(i.popleft())
        else:
            i.popleft()

    ans = []
    for h in list(i):
        if h in ans:
            pass
        else:
            ans.append(h)

    if ans==ess:
        print(f'#{n+1} YES')
    else:
        print(f'#{n+1} NO')

    




        


