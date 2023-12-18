from collections import deque
from sys import stdin

# n,m 입력받기
n,m = map(int,input().split())

# n * m 크기의 행렬 만들어주기. 단, m 크기만큼은 문자열로 주기 때문에 아래와 같이 구현
data_list = [[int(i) for i in stdin.readline().rstrip()] for _ in range(n)]
# 거리를 표현할 n * m 크기의 result 행렬 만들기
result = [[0 for _ in range(m)] for _ in range(n)]

# 처음에 시작하는 0,0 을 0으로 바꿔주기
data_list[0][0] = 0
# 처음에 시작하는 0,0 의 result 를 거리 1로 바꿔주기
result[0][0] = 1

# 방문하게 될 index의 편리한 계산을 위해 만들기
check_index = [[-1,0],[1,0],[0,-1],[0,1]]
# 방문해야하는 위치 담아둘 queue will_visit 만들기
will_visit = deque()

# bfs 구현
def bfs(x,y,cnt):
		# check_index 를 돌면서 순서대로 받아오기
    for temp in check_index:
				# 새롭게 방문할 index 정의
        new_x,new_y = x+temp[0], y+temp[1]
				
				# 행렬의 크기를 벗어나면 continue
        if new_x < 0 or new_y < 0 or new_x > n-1 or new_y > m-1:
            continue
				
				# 새롭게 방문할 위치의 값이 1이라면, result 의 위치에 거리(cnt)만큼 값을 부여
        if data_list[new_x][new_y] == 1:
            result[new_x][new_y] = cnt
						# 방문한 후 1의 값을 0으로 변경
            data_list[new_x][new_y] = 0
						# 다음에 방문 예정인 queue 에 추가
            will_visit.append([new_x,new_y,cnt+1])

# 처음 방문
# 이후에 will_visit 에는 첫 번째 노드에서 방문가능한 곳이 담겨 있음
# 또한 result 의 위 방문 가능한 곳에 거리만큼 표시가 됨
bfs(0,0,2)

# will_visit 에 빈값이 있기 전까지 무한 반복
while will_visit:
		# 방문 예정인 will_visit 에서 가장 먼저 들어온 값부터 뽑아오기
    temp = will_visit.popleft()
		
		# 방문 예정인 x,y,거리 값 받아오기
    x,y,cnt = temp[0], temp[1], temp[2]
		# bfs 수행
    bfs(x,y,cnt)
		
		# n-1, m-1 에 도달하면 반복문 탈출
    if x == n-1 and y == m-1:
        break

# 결과값 출력
print(result[n-1][m-1])