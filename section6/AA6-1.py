import sys
import heapq
#sys.stdin=open("input.txt", "r")

def solution(x):
    if x>0:
        solution(x//2)
        print(str(x%2),end='')
    
if __name__=="__main__":
    n = int(input())
    solution(n)









        


