#4.랜선자르기(결정알고리즘)

import sys
#sys.stdin=open("input.txt", "r")

k,n = map(int,input().split()) # k는 가지고 있는 랜선의 개수, n은 필요한 랜선의 개수
item = [int(input()) for _ in range(k)]

lt = 0
rt = max(item)
ans=[]
while lt<=rt:
    mid = (lt+rt)//2
    cnt = 0
    for i in item:
        cnt += i//mid
    if cnt < n:
        rt = mid-1
    elif cnt > n:
        lt = mid +1
        ans.append(mid)
    else:
        ans.append(mid)
        lt= mid+1
        

print(max(ans))










        





    
    







                












        










    
    






