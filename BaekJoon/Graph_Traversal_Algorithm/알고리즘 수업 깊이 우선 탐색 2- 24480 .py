from sys import stdin
from collections import deque
import sys
sys.setrecursionlimit(1000000)

n,m,v = map(int,stdin.readline().split())

dfs_queue = [deque() for _ in range(n+1)]

for _ in range(m):
    x,y = map(int, stdin.readline().split())
    dfs_queue[x].append(y)
    dfs_queue[y].append(x)

for i in range(n+1):
    dfs_queue[i] = deque(sorted(dfs_queue[i], reverse=True))

result = [0 for _ in range(n+1)]
check_visited = [False for _ in range(n+1)]

result[v] = 1
check_visited[v] = True
cnt = 2
def dfs(dfs_queue,v):
    global cnt
    global check_visited

    while True:
        try:
            temp = dfs_queue[v].popleft()
            if check_visited[temp] == False:
                check_visited[temp] = True
                result[temp] = cnt
                cnt += 1
                dfs(dfs_queue,temp)
        except:
            break

    return

dfs(dfs_queue, v)

for i in result[1:]:
    print(i)