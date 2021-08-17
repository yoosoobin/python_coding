import sys
#sys.stdin = open('input.txt','rt')
n = int(input())
mapp = []
for i in range(n):
    a = list(map(int,input().split()))
    a.append(0)
    a.insert(0,0)
    mapp.append(a)
zero = [[0]*(n+2)]
mapp= zero + mapp + zero

cnt = 0
for i in range(1,n+1):
    for j in range(1,n+1):
        if mapp[i][j]>mapp[i-1][j] and mapp[i][j]>mapp[i+1][j] and mapp[i][j]>mapp[i][j-1] and mapp[i][j]>mapp[i][j+1]:
            cnt +=1

print(cnt)







        










    
    






