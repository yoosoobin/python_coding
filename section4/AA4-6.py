#6. 씨름 선수(그리디)
import sys
#sys.stdin=open("input.txt", "r")
n = int(input())
players = [list(map(int,input().split())) for _ in range(n)]

players.sort(key = lambda x: (x[0],x[1]))
#print(players)  #키는 정렬되어 있으니까 뒤에 선수보다 몸무게가 작다면 탈락이다. (키는 볼 필요가 없다?)

ans = 0
for i in range(n):
    w  = players[i][1]
    #print(players[i],"심사시작","몸무게: ",w)
    for j in range(i+1,n):
        if players[j][1] >= w:
            #print( players[i],"은",players[j],"으로 인해 탈락")
            ans +=1
            break
        
        
print(n-ans)
    






    






        
        



            









        





    
    







                












        










    
    






