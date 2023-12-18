import sys
from collections import deque

deck = deque()
input = sys.stdin.readline

for _ in range(int(input())):
    temp = list(map(int,input().split()))
    
    if temp[0] == 1: deck.appendleft(temp[1])
    elif temp[0] == 2: deck.append(temp[1])
    elif temp[0] == 3: print(deck.popleft()) if deck else print(-1)
    elif temp[0] == 4: print(deck.pop()) if deck else print(-1)
    elif temp[0] == 5: print(len(deck))
    elif temp[0] == 6: print(0) if deck else print(1)
    elif temp[0] == 7: print(deck[0]) if deck else print(-1)
    elif temp[0] == 8: print(deck[-1]) if deck else print(-1)