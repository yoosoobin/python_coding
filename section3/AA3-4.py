import sys
#sys.stdin = open('input.txt','rt')
fn = int(input())
f = list(map(int,input().split()))
sn = int(input())
s = list(map(int,input().split()))
sum_num = []
p1,p2 = 0,0
while True:
    if p1==fn:
        for i in s[p2:]:
            sum_num.append(i)
        break
    elif p2 == sn:
        for i in f[p1:]:
            sum_num.append(i)
    elif f[p1] <= s[p2]:
        sum_num.append(f[p1])
        p1 +=1
    else:
        sum_num.append(s[p2])
        p2 +=1

for i in sum_num:
    print(i,end=' ')
