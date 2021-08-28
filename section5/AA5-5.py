import sys
from collections import deque
#sys.stdin=open("input.txt", "r")
n,k = map(int,input().split())

prince = [i for i in range(1,n+1)]


prince = deque(prince)

while len(prince) >=2:
    for i in range(k-1):
        prince.append(prince.popleft())
    prince.popleft()

for i in prince:
    print(i)







