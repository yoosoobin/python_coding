import sys
#sys.stdin = open('input.txt','rt')
fn = int(input())
f = list(map(int,input().split()))
sn = int(input())
s = list(map(int,input().split()))

sum_list = f+s
for i in sorted(sum_list):
    print(i,end=' ')
