import sys
from collections import deque
#sys.stdin=open("input.txt", "r")
n,m = map(int,input().split())
num = list(map(int,input().split()))
num = [(n,i) for (n,i) in enumerate(num)]
num = deque(num)


cnt = 0
while True:
    cur = num.popleft()
    if any(cur[1]<x[1] for x in num):
        num.append(cur)
    else:
        cnt +=1
        if cur[0] == m:
            print(cnt)
            break
        




        


