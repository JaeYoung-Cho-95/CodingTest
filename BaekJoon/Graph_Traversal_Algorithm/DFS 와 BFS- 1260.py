from sys import stdin
from collections import deque
n,m,v = map(int, input().split())
data_list = [deque() for _ in range(n+1)]

for _ in range(m):
    x,y = map(int, input().split())
    data_list[x].append(y)
    data_list[y].append(x)

data_list = [deque(sorted(x)) for x in data_list]

result_bfs = [str(v)]
result_dfs = [str(v)]

bfs_check_visit = [False for _ in range(n+1)]
dfs_check_visit = [False for _ in range(n+1)]

bfs_check_visit[v] = True
dfs_check_visit[v] = True

go_visit = deque()
go_visit.extend(data_list[v])

while True:
    if len(go_visit) == 0:
        break

    temp = go_visit.popleft()

    if bfs_check_visit[temp] == False:
        bfs_check_visit[temp] = True
        result_bfs.append(str(temp))
        go_visit.extend(data_list[temp])


def dfs(data_list,v):
    global cnt

    while True:
        if len(data_list[v]) == 0:
            break

        temp = data_list[v].popleft()

        if dfs_check_visit[temp] == False:
            dfs_check_visit[temp] = True
            result_dfs.append(str(temp))
            dfs(data_list, temp)

dfs(data_list,v)

print(' '.join(result_dfs))
print(' '.join(result_bfs))