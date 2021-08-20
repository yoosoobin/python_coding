#5. 뮤직비디오 (결정알고리즘)
import sys
#sys.stdin=open("input.txt", "r")

n,m = map(int,input().split())
song = list(map(int,input().split()))

mn = 1
mx = sum(song)

ans = []
while mn<=mx:
    mid = (mn+mx)//2
    sum=0
    cnt=0
    for i in song:
        if sum <mid:
            sum+=i
            if sum > mid:
                cnt +=1
                sum = i
            elif sum ==mid:
                cnt +=1
                sum = 0
            else:
                pass
    if sum >0:
        cnt += 1
           
    if cnt > m :
        mn = mid+1
    elif cnt < m:
        ans.append(mid)
        mx = mid -1
    else:
        ans.append(mid)
        mx = mid -1

print(min(ans))




            









        





    
    







                












        










    
    






