import sys
#sys.stdin=open("input.txt", "r")

def DFS(L,s):
    global cnt
    if L == m :
        total = 0
        for i in res:
            total+=i
        if total%sum == 0:
            cnt+=1
    else:
        for i in range(s,n+1):
            res[L]=num_list[i-1]
            DFS(L+1,1+i)
  
      
if __name__=="__main__": 
    n,m = map(int,input().split())
    num_list = list(map(int,input().split()))
    sum = int(input())
    res = [0]*m
    cnt = 0
    DFS(0,1)
    print(cnt)
    

         

    


    
    
    
    

   


 






        


