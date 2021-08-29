import sys
from collections import deque
#sys.stdin=open("input.txt", "r")
n = int(input())
words = [input() for _ in range(n)]
use = [input() for _ in range(n-1)]

for i in use:
    if i in words:
        words.remove(i)
    else:
        pass
for j in words:
    print(j)



    




        


