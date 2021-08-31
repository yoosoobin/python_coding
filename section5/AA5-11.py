import sys
import heapq
#sys.stdin=open("input.txt", "r")

mx = 0
heap =[]
heapq.heapify(heap)

while True:
    a = int(input())
    if a== -1:
        break
    elif a!=0:
        heapq.heappush(heap,a)
    else:
        heap.sort()
        if len(heap) == 0:
            print(-1)
        else:
            print(heap.pop())





        


