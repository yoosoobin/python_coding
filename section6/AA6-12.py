import sys
import itertools as it
#sys.stdin=open("input.txt", "r")

n,m = map(int,input().split())
a = [list(map(int,input().split())) for _ in range(m) ]
ch = [[0]*n for _ in range(n)]    
    

for i in a:
    ch[i[0]-1][i[1]-1]=i[2]
        
for j in ch:
    for h in j:
        print(h,end=' ')
    print()


    


    
    
    
    

   


 






        


