import sys
#sys.stdin = open('input.txt','rt')
n = int(input())
farm = [list(map(int,input().split())) for _ in range(n)]
m = int(input())
order = [list(map(int,input().split())) for _ in range(m)]

for i in order:
    if i[1]==0:
        for j in range(i[2]):
            farm[i[0]-1].append(farm[i[0]-1].pop(0))
    else:
        for j in range(i[2]):
            ans = []
            ans.append(farm[i[0]-1].pop())
            farm[i[0]-1] = ans + farm[i[0]-1]

s=0
e=n-1
sum=0
for i in range(n):
    if i< n//2:
        for j in range(s,e+1):
            sum += farm[i][j]
        s+=1
        e-=1
        
    else:
        for j in range(s,e+1):
            sum+=farm[i][j]
        s-=1
        e+=1
print(sum)
        










    
    






