import heapq
import sys

x = []
for _ in range(int(input())):
    tmp = int(sys.stdin.readline())
    heapq.heappush(x, tmp)

cnt = 0

while len(x) > 1:
    tmp_1 = heapq.heappop(x)
    tmp_2 = heapq.heappop(x)

    sum_tmp = tmp_1 + tmp_2
    cnt += sum_tmp
    heapq.heappush(x, sum_tmp)

print(cnt)
