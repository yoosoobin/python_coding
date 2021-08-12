
import sys
import collections
#sys.stdin = open('input.txt','rt')

n = int(input())
n_list = list(map(int,input().split()))

cnt = 1
score= 0
for i in n_list:
    if i==1:
        score += cnt
        cnt +=1
    else:
        cnt = 1

print(score)







    



