
import sys
#sys.stdin = open('input.txt','rt')
n = int(input())

for i in range(n):
    N,s,e,k = map(int,input().split())
    num_list = list(map(int,input().split()))
    num_list = num_list[s-1:e]
    num_list.sort()
    print('#{} {}'.format(i+1,num_list[k-1]))