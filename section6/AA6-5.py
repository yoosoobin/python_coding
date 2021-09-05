import sys
#sys.stdin=open("input.txt", "r")

def DFS(v,sum,tsum):
    global ans
    if sum + (total-tsum)<ans:
        return
    if sum>max:
        return
    if v==n:
        if sum>ans:
            ans = sum
    else:
        DFS(v+1,sum+dogs[v],tsum+dogs[v])
        DFS(v+1,sum,tsum+dogs[v])

    
if __name__=="__main__": 
    max,n = map(int,input().split())# 태울 수 있는 최대 무게 
    dogs = list(int(input()) for _ in range(n))
    ans = 0
    total =sum(dogs)
    DFS(0,0,0)
    print(ans)
    

   


 






        


