from sys import stdin
import heapq
# N = int(stdin.readline().rstrip())
N = int(input())
result_heap_list = []
for i in range(N):
    # a = int(stdin.readline().rstrip())
    a = int(input())
    if a == 0:
        try:
            print(heapq.heappop(result_heap_list)[1])
        except:
            print(0)
    else:
        heapq.heappush(result_heap_list, (-a, a))