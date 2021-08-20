import sys
#sys.stdin=open("input.txt", "r")
n,m = map(int, input().split())
num = list(map(int,input().split()))
num.sort()


lt = 0
rt = n-1

while True:
    mid = (lt+rt)//2 
    if num[mid]==m:
        print(mid+1)
        break
    elif num[mid] > m:
        rt = mid-1
    else:
        lt = mid +1



        





    
    







                












        










    
    






