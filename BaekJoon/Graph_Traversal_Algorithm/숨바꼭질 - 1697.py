# 사실 함수자체가 bfs 는 아니고, 그냥 x 값과 시간초 값을 받아와서 방문 예정인 queue 에 x-1, x+1, 2*x 를 추가해준다
def bfs(x,cnt):
    will_visit.append([x-1,cnt])
    will_visit.append([x+1,cnt])
    will_visit.append([2*x,cnt])

from collections import deque

x,y = map(int, input().split())

# x와 y값이 같다면 0초
if x == y:
    print(0)
else:
		# x가 y 보다 크다면 x-y 초
    if x > y:
        print(x - y)
		# x 가 y 보다 작다면
    if x < y:
				# 이미 방문한 곳에는 y+3 까지 넉넉하게 False 로 채워주기
				# 2x 의 값이 y + 1 이 되어 그 다음에 방문하여 도달하게 될 경우도 있기 때문에
        already_visited = [False for _ in range(y+3)]
				# 방문 예정인 queue 에는 첫 번째 경우에 대해서만 미리 담아 놓기
				# 시간초 또한 담아 놓기
        will_visit = deque([[x-1,1],[x+1,1],[2*x,1]])
				
				# 무한루프를 돌림
        while True:
						# 방문 예정인 queue 에서 첫 번째 인자값을 뽑아옴
            temp, cnt = will_visit.popleft()
						
						# 만약, temp 가 0보다 작거나 y + 2 보다 작으면 continue(방문할 필요가 없음)
            if (temp < 0) or (temp > (y+2)):
                continue
						# 아직 방문한 적이 없다면 방문했다고 바꾸고 해당 위치에서 bfs 돌리기
            if already_visited[temp] == False:
                already_visited[temp] = True
                bfs(temp, cnt+1)
						# 만약 뽑아온 temp 가 y 위치에 도달했다면 반복문 탈출
            if temp == y:
                break
				
				# cnt 출력
        print(cnt)