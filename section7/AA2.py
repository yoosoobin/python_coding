## 휴가(삼성 SW역량평가 기출문제: DFS활용)

import sys
#sys.stdin=open("input.txt", "r")
def DFS(L,sum):
    global res
    if L==n+1:
        if sum > res:
            res = sum
    else:
        if L+T[L]<=n+1:
            DFS(L+T[L],sum+P[L])
        DFS(L+1,sum)

  
if __name__ == '__main__':
    n = int(input())
    T = list()
    P = list()
    for i in range(n):
        a,b = map(int,input().split())
        T.append(a)
        P.append(b)
    res = -2147000000
    T.insert(0,0)  #인덱스 번호를 날짜로 사용하기 위해 
    P.insert(0,0)
    DFS(1,0)
    print(res)




    


    
    
    
    

   


 






        


