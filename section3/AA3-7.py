import sys
#sys.stdin = open('input.txt','rt')
n = int(input())
farm = [list(map(int,input().split())) for _ in range(n)]

a_sum = 0
m = n//2

for i in range(n):
    if i<= m:
        a_sum += sum(farm[i][m-i:m+i+1])
    else:
        a_sum += sum(farm[i][i-m:m+(n-i)])
        
print(a_sum)

            






