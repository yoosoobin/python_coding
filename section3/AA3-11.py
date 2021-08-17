import sys
#sys.stdin=open("input.txt", "r")

dx=[1,0]
dy=[0,1]

def find(x):
    cnt=0
    for i in range(7):
        for j in range(3):
            a = x[i][j:j+5]
            b = list(x[j+k][i] for k in range(5))
            if a[0]==a[-1] and a[1]==a[-2]:
                cnt +=1
            if b[0]==b[-1] and b[1]==b[-2]:
                cnt +=1
    return cnt

data = list(list(map(int,input().split())) for _ in range(7))
print(find(data))


        





    
    







                












        










    
    






