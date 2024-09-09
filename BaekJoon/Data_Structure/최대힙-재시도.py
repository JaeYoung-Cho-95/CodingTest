import heapq
import sys

n = int(sys.stdin.readline())
x = []

for _ in range(n):
    i = int(sys.stdin.readline()) * -1
    
    if i == 0:
        try:
            print(heapq.heappop(x) * -1)
        except:
            print(0)
        continue
    else:
        heapq.heappush(x, i)