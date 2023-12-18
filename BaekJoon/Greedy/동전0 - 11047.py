
from sys import stdin

N,K = map(int, stdin.readline().rstrip().split())
# N,K = map(int, input().split())

value = [int(stdin.readline().rstrip()) for _ in range(N)]
# value = [int(input()) for _ in range(N)]

cnt = 0
index = len(value) - 1
while True:
    if K // value[index] >= 1:
        cnt += K // value[index]
        K = K % value[index]
    else:
        index -= 1

    if K == 0:
        break

print(cnt)