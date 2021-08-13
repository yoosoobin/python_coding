import sys
#sys.stdin = open('input.txt','rt')
card_list= [i for i in range(1,21)]

for i in range(10):
    s,e = map(int,input().split())
    copy = card_list[s-1:e] 
    copy.reverse()
    card_list[s-1:e] = copy

for i in card_list:
    print(i,end=' ')
