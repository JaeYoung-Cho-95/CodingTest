from collections import deque
from sys import stdin

# x,y 행렬의 크기 입력받기
x,y = map(int,input().split())

# 행렬의 크기만큼 토마토 입력 받기
result = [list(map(int, stdin.readline().rstrip().split())) for _ in range(y)]

# 행렬 크기만큼 방문여부 체크를 위해 True 로 채워주기
check_visited = [[True for i in range(x)] for _ in range(y)]

# 방문예정인 queue 생성
will_visit = deque()

# 처음에 방문예정인 곳 정하기 위해 행렬을 모두 돌게됨
# 0이 아닌 경우 방문여부 체크에 모두 False 로 바꿔줌
# 그 중 1인 경우 방문예정인 queue 에 행렬의 위치와 day (0)값 넣기
for i in range(x):
    for j in range(y):
        if result[j][i] != 0:
            check_visited[j][i] = False
            if result[j][i] == 1:
                will_visit.append([j,i,0])

# 행렬의 위치값과 day 를 입력받아 
# check_visited 에서 True (즉, 아직 방문하지 않았으면서 비어있지 않은 곳) 
# 그리고 result 에서 0 값이라면, 방문예정인 queue 에 추가해준다
def bfs(j,i,day):
		# 행렬의 크기 밖으로 나가면 None 반환
    if j < 0 or i < 0 or j > y-1 or i > x-1:
        return
    else:
        if (check_visited[j][i] == True) and (result[j][i] == 0):
            check_visited[j][i] = False
            result[j][i] = 1
            will_visit.append([j,i,day+1])

# 만약 방문 예정인 곳의 queue 의 길이가 0이라면, 익은 토마토가 하나도 없다는 뜻으로 -1 출력
if len(will_visit) == 0:
      print(-1)
else:
    while True:
				# 행렬의 위치와 day 를 받아와서 상하좌우의 위치에 bfs 돌려주기
        j,i,day = will_visit.popleft()
        bfs(j-1,i,day)
        bfs(j+1,i,day)
        bfs(j,i-1,day)
        bfs(j,i+1,day)
				
				# 더 이상 방문할 수 있는 queue의 데이터가 존재하지 않다면 break
        if len(will_visit) == 0:
            break
		
    check = True
		# check_visited 를 순회하면서 각 행을 더해주고 0보다 크면 아직 방문하지 못하고 익지 않은 토마토가 있다는 의미로 check = False
    for i in range(y):
        if sum(check_visited[i]) > 0:
            check = False
		# check = True, 즉 모두 익은 토마토라면 day 를 출력
    if check:
        print(day)
    else:
        print(-1)