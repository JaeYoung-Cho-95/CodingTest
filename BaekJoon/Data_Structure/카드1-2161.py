from collections import deque
from sys import stdin

n = int(input())
x = deque([x for x in range(1, n + 1)])

while True:
    if len(x) == 1:
        break
    
    print(x.popleft())
    x.append(x.popleft())
    
print(x[0])