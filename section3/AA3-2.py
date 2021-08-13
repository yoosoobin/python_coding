
import sys
import collections
#sys.stdin = open('input.txt','rt')
s = list(input())

ans =''
for i in s:
  try:
    int(i)
  except:
    pass
  else:
    ans+=i

a=0
for i in  range(len(ans)):
  if ans[i] == '0':
    a+=1
  else:
    break
ans=int(ans[a:])

n_list=[]
for i in range(1,ans//2+1):
    if ans%i == 0:
        n_list.append(i)
print(ans,len(n_list)+1,sep='\n')





    






