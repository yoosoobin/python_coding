import sys
#sys.stdin = open('input.txt','rt')
n = int(input())
pan = []
for _ in range(n):
    pan.append(list(map(int,input().split())))

sum_list=[]
def sum_row(x):
    for i in x:
        sum_list.append(sum(i))

def sum_col(x):
    sum_dic={}
    for i in x:
        for j in range(len(x)):
            if j in sum_dic:
                sum_dic[j]+= i[j]
            else:
                sum_dic[j] = i[j]
    for i in range(len(x)):
        sum_list.append(sum_dic[i])

def sum_x(x):
    sum_l=0
    sum_r=0
    for n,i in enumerate(x):
        sum_l += i[n]
        sum_r += i[len(x)-n-1]
    sum_list.append(sum_l)
    sum_list.append(sum_r)


sum_row(pan)
sum_col(pan)
sum_x(pan)

ans = max(sum_list)
print(ans)


        






