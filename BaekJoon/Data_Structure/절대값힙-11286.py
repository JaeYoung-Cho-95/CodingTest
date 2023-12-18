from heapq import heappush, heappop
import sys

n = int(input())
heapq_= []
answer = ""

for _ in range(n):
    x = int(sys.stdin.readline())
    if (x == 0):
        if heapq_:     
            answer += f"{heappop(heapq_)[1]}\n"
        else:
            answer += "0\n"
        
    else:
        heappush(heapq_,[abs(x),x])

print(answer.rstrip("\n"))