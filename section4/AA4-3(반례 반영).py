#5. 뮤직비디오 (결정알고리즘)
import sys
sys.stdin=open("input.txt", "r")

def Count(capacity):
    cnt = 1
    sum = 0
    for x in song:
        if sum + x > capacity:
            cnt +=1
            sum = x
        else:
            sum +=x
    return cnt

n,m = map(int,input().split())
song = list(map(int,input().split()))
maxx = max(song)

lt=1
rt = sum(song)
res = 0

while lt<=rt:
    mid=(lt+rt)//2
    if mid>=maxx and Count(mid)<=m:
        res = mid
        rt = mid-1
    else:
        lt = mid +1


print(res)


            









        





    
    







                












        










    
    






