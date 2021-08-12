
import sys
import collections
#sys.stdin = open('input.txt','rt')

n = int(input())
for i in range(n):
    s = list(input().lower())   
    r = list(reversed(s)) 
    if s == r:
        print('#{} YES'.format(i+1))
    else:
        print('#{} NO'.format(i+1))



