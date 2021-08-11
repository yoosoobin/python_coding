
import sys
#sys.stdin = open('input.txt','rt')
n = int(input())
score = list(map(int, input().split()))
avg = int(round(sum(score)/len(score),0))

dif = []
for s in score:
    dif.append(s-avg)
    
ans = float('inf')
stu_num = 0
for n,d in enumerate(dif): 
    if abs(d) < abs(ans):
        ans = d
        stu_num = n+1
       
    elif abs(d) == abs(ans):
        if d > ans:
            ans = d
            stu_num = n+1

print(avg,stu_num)
