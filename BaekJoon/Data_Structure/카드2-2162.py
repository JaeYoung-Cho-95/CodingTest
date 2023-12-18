from sys import stdin
from collections import deque

# N = int(stdin.readline().rstrip())

N = int(input())
Q_ = deque([i for i in range(2,N+1,2)])

if len(Q_) == 0:
    print(1)

else:
    if N % 2 == 0:
        cnt = 0
    else:
        cnt = 1

    while True:
        if len(Q_) == 1:
            print(Q_.popleft())
            break
        
        if cnt % 2 == 0:
            Q_.popleft()
        else:
            Q_.append(Q_.popleft())
            
        cnt += 1