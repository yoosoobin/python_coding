
import sys
#sys.stdin = open('input.txt','rt')
n,m = map(int, input().split())

sum_list = {}

for i in range(1,n+1):
    for j in range(1,m+1):
        plus = i+j
        if plus in sum_list:
            sum_list[plus]+=1
        else:
            sum_list[plus] =1

max = 0
ans =[]
for i in sum_list:
    if sum_list[i] > max:
        max = sum_list[i]
for i in sum_list:
    if sum_list[i] == max:
        ans.append(i)

for i in ans:
    print(i,end = ' ')







