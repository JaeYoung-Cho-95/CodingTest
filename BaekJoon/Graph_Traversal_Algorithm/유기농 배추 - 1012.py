from sys import stdin
from collections import deque
import sys
# 파이썬 재귀 재한 늘리기
sys.setrecursionlimit(10000000)

# dfs 구현하기
def dfs(x,y):
    global data_list
		# 만약, x,y가 0보다 작거나 n-1,m-1 보다 크다면 함수 종료
    if (x < 0) or (x > n-1) or (y < 0) or (y > m-1):
        return

		# 만약, [x][y]가 1이라면 사방에 1이 또 있는지 확인
    if data_list[x][y] == 1:
        data_list[x][y] = 0
        dfs(x-1,y)
        dfs(x+1,y)
        dfs(x,y-1)
        dfs(x,y+1)

    else:
        return


N = int(input())
result = []
for i in range(N):
    n,m,v = map(int, input().split())
		
		# data_list 만들어주기
    data_list = [[0 for _ in range(m)] for _ in range(n)]
    count = 0
		
		# 배추가 심어진 곳 1로 바꿔주기
    for _ in range(v):
        x,y = map(int, input().split())
        data_list[x][y] = 1
		
		# 순서대로 방문하면서 만약, 해당 인덱스의 값이 1이라면 dfs 로 돌리기
    for row in range(n):
        for col in range(m):
            temp = data_list[row][col]
            if temp == 1:
                data_list[row][col] = 0
								# 배추벌레 숫자 추
                count += 1
                dfs(row-1,col)
                dfs(row+1,col)
                dfs(row,col-1)
                dfs(row,col+1)

    result.append(count)

for i in result:
    print(i)