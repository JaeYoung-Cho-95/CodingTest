import heapq
from sys import stdin

heap = []
N = int(input())

for i in range(N):
    # i = int(stdin.readline().rstrip())
    i = int(input())
    if i == 0:
        try:
            print(heapq.heappop(heap))
        except:
            print(0)
    else:
        heapq.heappush(heap, i)