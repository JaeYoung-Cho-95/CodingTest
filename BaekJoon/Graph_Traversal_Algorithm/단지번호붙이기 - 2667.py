# dfs 구현
def dfs(x, y):
		# global 변수 받기
    global cnt
    global data_list
		# 만약, x , y 가 0보다 작거나 N-1 보다 크다면 return
    if (x < 0) or (x > N-1) or (y < 0) or (y > N-1):
        return
    elif data_list[x][y] == '1':
        data_list[x][y] = '0'
        cnt += 1
        dfs(x-1,y)
        dfs(x+1,y)
        dfs(x,y-1)
        dfs(x,y+1)

    elif data_list[x][y] == '0':
        return

# 첫 줄에 입력받는 N
N = int(input())

# data_list 만들어주기
data_list = []
result = []
count = 0

from sys import stdin
# 데이터 입력받아서 data_list 안에 채워주기
for i in range(N):
    x = list(stdin.readline().rstrip())
    data_list.append(x)

# data_list 에서 row 값 받아오기
for row in range(N):
	# row 에 있는 col 값 받아오기
    for col in range(N):
			# 만약 data_list[row][col] 의 값이 1이면 dfs 시작
        if data_list[row][col] == '1':
						# 일단 row col 에 해당하는 1을 0으로 바꾸기
						# 그래야지 다음에 다시 방문 안함
            data_list[row][col] = '0'
						# 몇 개가 연결되어 있는지 확인할 수 있는 cnt 생성
            cnt = 1
						# 총 단지의 수 더해주기
            count += 1
						# dfs 에 row, col 에 -1, +1 돌아가면서 재귀돌려주기
            dfs(row-1,col)
            dfs(row+1,col)
            dfs(row,col-1)
            dfs(row,col+1)
						
						# dfs 안에서 global 변수로 받아서 더해주는 cnt 마지막에 result 에 담아주기 
            result.append(cnt)


print(count)
result = sorted(result)
for i in result:
    print(i)