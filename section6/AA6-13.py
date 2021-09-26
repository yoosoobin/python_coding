## 경로탐색(그래프 DFS)

import sys
sys.stdin=open("input.txt", "r")

def DFS(a):
    global n
    global cnt
    if a==n:
        cnt+=1

    else:
        for i in range(1,n+1):
            if ch[a-1][i-1]!=0 and visit[i-1]==0:
                visit[i-1]=1
                DFS(i)
                visit[i-1]=0

if __name__ == '__main__':
    n,m = map(int,input().split())
    ch = [[0]*n for _ in range(n)]
    for i in range(m):
        a,b = map(int,input().split())
        ch[a-1][b-1]=b
    visit = [0]*n
    visit[0]=1
    cnt=0
    DFS(1)
    print(cnt)



    


    
    
    
    

   


 






        


