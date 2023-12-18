from collections import deque
import sys
from sys import stdin
sys.setrecursionlimit(10000000)

n,m,v = map(int, stdin.readline().split())

dfs_list = [deque() for _ in range(n+1)]

for i in range(m):
    x,y = map(int, stdin.readline().split())
    dfs_list[x].append(y)
    dfs_list[y].append(x)

for i in range(len(dfs_list)):
    dfs_list[i] = deque(sorted(dfs_list[i]))

check_visited = [True] + [False for _ in range(n)]
result = [0 for _ in range(n+1)]

check_visited[v] = True
result[v] = 1

count = 2

def dfs(dfs_list,v,check_visited):
    global count

    while True:
        try:
            temp = dfs_list[v].popleft()
            if check_visited[temp] == False:
                check_visited[temp] = True
                result[temp] = count
                count += 1
                dfs(dfs_list, temp, check_visited)
        except:
            break
    return None

dfs(dfs_list,v,check_visited)

for i in result[1:]:
    print(i)