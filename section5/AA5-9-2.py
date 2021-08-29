# 딕셔너리가 아닌 리스트를 활용한 풀이 (ASCII를 이용)

import sys
from collections import deque
sys.stdin=open("input.txt", "r")
a = input()
b = input()
str1=[0]*52
str2=[0]*52

for x in a:
    if x.isupper():
        str1[ord(x)-65]+=1
    else:
        str1[ord(x)-71]+=1

for x in b:
    if x.isupper():
        str2[ord(x)-65]+=1
    else:
        str2[ord(x)-71]+=1

for i in range(52):
    if str1[i]!=str2[i]:
        print('NO')
        break
    
print('YES')





        





        


