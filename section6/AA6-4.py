import sys
import heapq
#sys.stdin=open("input.txt", "r")

def DFS(L,sum):
    if sum >total//2:  #시간복잡도 줄이기 
        return
    if L==n:
        if sum == total - sum:
            print("YES")
            sys.exit(0)
    else:
        DFS(L+1,sum+a[L])  #a리스트에 L인덱스 원소를 부분집합에 원소로 사용한다는 의미
        DFS(L+1,sum)
        

    
if __name__=="__main__": 
    n = int(input())
    a = list(map(int,input().split()))
    total = sum(a)
    DFS(0,0)
    print('NO')


 






        


