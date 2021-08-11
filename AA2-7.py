
import sys
#sys.stdin = open('input.txt','rt')
n = int(input())

def solution(n):
    cnt = 0
    for i in range(1,n+1):
        if i ==1:
            pass
        elif i in [2,3]:
            cnt +=1
        else:
            limit = int(i**0.5)
            count = 0
            for j in range(2,limit+1):
                if i%j == 0:
                    break
                else: 
                    count += 1
            if count == limit-1:
                cnt += 1
            
    return cnt

print(solution(n))

    



