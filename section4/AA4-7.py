#7. 창고 정리
import sys
#sys.stdin=open("input.txt", "r")
l = int(input())
num = list(map(int,input().split()))
o = int(input())

num.sort(reverse = True)


while o>0:
    num[0]-=1
    num[-1]+=1
    o-=1
    num.sort(reverse =True)

print(num[0]-num[-1])




    






        
        



            









        





    
    







                












        










    
    






