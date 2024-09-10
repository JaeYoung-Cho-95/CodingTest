import heapq
from sys import stdin

for i in range(int(stdin.readline())):
    max_x, min_x = [], []
    for _ in range(int(stdin.readline())):
        cndi, num = stdin.readline().split(" ")

        if cndi == "I":
            heapq.heappush(min_x, int(num))
            heapq.heappush(max_x, int(num) * -1)

        if cndi == "D":
            try:
                if int(num) == 1:
                    heapq.heappop(max_x)
                    continue

                heapq.heappop(min_x)
            except:
                pass

    if len(min_x) + len(max_x) < i:
        print("EMPTY")
    else:
        print(f"{heapq.heappop(max_x) * -1} {heapq.heappop(min_x)}")
