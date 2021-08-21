#6. 회의실 배정(그리디)
import sys
#sys.stdin=open("input.txt", "r")

n = int(input())
plan = [list(map(int,input().split())) for _ in range(n)]
plan.sort(key=lambda x : (x[1], x[0]))  # x[0]으로 오름차순, x[1]로 오름차순 적용
 
s,e= plan[0][0], plan[0][1]

cnt = 1
for i in plan:
    if i[0] >= e:
        cnt +=1
        e = i[1]

print(cnt)







        
        



            









        





    
    







                












        










    
    






