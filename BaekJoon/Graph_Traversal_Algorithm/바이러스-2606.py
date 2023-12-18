from collections import deque
N = int(input())
M = int(input())

data_list = [deque() for _ in range(N+1)]

for i in range(M):
  x,y = map(int,input().split())
  data_list[x].append(y)
  data_list[y].append(x)

data_list = [deque(sorted(x)) for x in data_list]
check_visited = [False for _ in range(N+1)]

check_visited[1] = True
cnt = 0

def dfs(data_list, st_index):
  global cnt

  while True:
    if len(data_list[st_index]) == 0:
      break

    temp = data_list[st_index].pop()
    if check_visited[temp] == False:
      check_visited[temp] = True
      cnt += 1
      dfs(data_list, temp)
    
  return

dfs(data_list, 1)
print(cnt)