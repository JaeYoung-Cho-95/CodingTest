import heapq
import sys


n = int(input())
x = []

for _ in range(n):
    n = int(sys.stdin.readline())
    if n == 0:
        try:
            print(heapq.heappop(x))
        except:
            print(0)
        continue
    else:
        heapq.heappush(x, n)
