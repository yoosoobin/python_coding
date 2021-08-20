#5. 마구간 정하기(결정알고리즘)
import sys
#sys.stdin=open("input.txt", "r")


def count(distance):
    cnt = 1
    mol = 1
    for i in dis:
        if i-mol >= distance:
            cnt+=1
            mol = i
        else:
            pass
    return cnt 

n,c = map(int,input().split())
dis  = [int(input()) for _ in range(n)]
dis.sort()


mn= dis[1]-dis[0] # 가장 가까이 있을경우 거리 차이

mx = dis[-1]-dis[0] #가장 멀리 있을경우 거리차이

res = 0
while mn<=mx:
    mid = (mn+mx)//2
    if count(mid) <c:
        mx = mid-1
    else:
        res=mid
        mn = mid +1

print(res)





        
        



            









        





    
    







                












        










    
    






