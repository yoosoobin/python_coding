#7. 침몰하는 타이타닉(그리디)
import sys
#sys.stdin=open("input.txt", "r")

n,m = map(int,input().split())
wlist = list(map(int,input().split()))

wlist.sort()

cnt = 0

while len(wlist) > 1 :
    if wlist[0]+wlist[-1] <=m:
        wlist.pop(0)
        wlist.pop(-1)
        cnt+=1

    else:
        wlist.pop(-1)
        cnt +=1
if len(wlist) != 0:
    cnt+=1
print(cnt)





    






        
        



            









        





    
    







                












        










    
    






