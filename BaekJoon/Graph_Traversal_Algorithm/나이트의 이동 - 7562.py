def bfs(go_x, go_y):
    if (go_x < 0) or (go_y < 0) or (go_x > n-1) or (go_y > n-1):
        return

    if data_list[go_x][go_y] == False:
        data_list[go_x][go_y] = True
        go_list.append([go_x,go_y,cnt])

from collections import deque
from sys import stdin
for _ in range(int(input())):
    n = int(stdin.readline().rstrip())
    # n = int(input())

    data_list = [[False for _ in range(n)] for _ in range(n)]

    start_x, start_y = map(int, stdin.readline().rstrip().split())
    # start_x, start_y = map(int, input().split())

    end_x, end_y = map(int, stdin.readline().rstrip().split())
    # end_x, end_y = map(int, input().split())

    cnt = 0
    data_list[start_x][start_y] = True
    go_list = deque([[start_x,start_y,cnt]])

    if start_x == end_x and start_y == end_y:
        print(0)
    else:
        while True:
            go_x, go_y, cnt = go_list.popleft()
            if (go_x == end_x) and (go_y == end_y):
                break
            else:
                cnt += 1
                bfs(go_x-2,go_y-1)
                bfs(go_x-1,go_y-2)
                bfs(go_x+1,go_y-2)
                bfs(go_x+2,go_y-1)
                bfs(go_x-2,go_y+1)
                bfs(go_x-1,go_y+2)
                bfs(go_x+1,go_y+2)
                bfs(go_x+2,go_y+1)

        print(cnt)