from collections import deque
from sys import stdin
n,m,r = map(int, stdin.readline().split())

# 0번째 노드를 포함하여 생성(0번째 노드는 사용 X)
graph_list = [deque() for _ in range(n+1)]

# 간선의 수만큼 입력받기
# 양방향 간선이기 때문에 양쪽 다 채워주기
for i in range(m):
    x,y = map(int, stdin.readline().split())
    graph_list[x].append(y)
    graph_list[y].append(x)

# 오름차순 정렬
graph_list = [deque(sorted(x)) for x in graph_list]

check_visit = [False for _ in range(n+1)]
result = [0 for _ in range(n+1)]
go_visit = deque()

check_visit[r] = True

go_visit.extend(graph_list[r])
result[r] = 1
cnt = 2

while True:
    if len(go_visit) == 0:
        break

    temp = go_visit.popleft()
    if check_visit[temp] == False:
        check_visit[temp] = True
        go_visit.extend(graph_list[temp])
        result[temp] = cnt
        cnt += 1

for i in result[1:]:
    print(i)