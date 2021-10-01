## 양팔저울(DFS)

import sys
#sys.stdin=open("input.txt", "r")
def DFS(L,sum):
    if L==k :
        if sum >0:
            ans.append(sum)    
    else:
        DFS(L+1,sum+w[L])
        DFS(L+1,sum)
        DFS(L+1,sum-w[L])

if __name__ == '__main__':
    k = int(input())
    w = list(map(int,input().split()))
    s = sum(w)
    ans = list()
    DFS(0,0)
    make = list(set(ans))
    res = list(i for i in range(1,s+1))
    cnt = 0
    for i in res:
        if i not in make:
            cnt+=1
    print(cnt)





    


    
    
    
    

   


 






        


