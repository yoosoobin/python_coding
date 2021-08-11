
import sys
#sys.stdin = open('input.txt','rt')
n = int(input())
num = list(map(int,input().split()))

def digit_sum(x):
    x = str(x)
    ans = 0
    for i in range(len(x)):
        ans += int(x[i])
    return ans       

max = 0
for i in num:
    if digit_sum(i) > max:
        max = digit_sum(i)
        ans = i

print(ans)
    



