from sys import stdin
n = int(input())
tree = {}
for i in range(n-1):
    x,y = map(int, stdin.readline().rstrip().split())
    try:
        tree[x].append(y)
    except:
        tree[x] = [y]
    try:
        tree[y].append(x)
    except:
        tree[y] = [x]


from collections import deque
go_visit = deque([[1,tree[1]]])

result = [0,1] + [False for _ in range(2,n+1)]

while True:
    if len(go_visit) == 0:
        break

    parent, babys = go_visit.popleft()

    for baby in babys:
        if result[baby] == False:
            result[baby] = parent
            go_visit.append([baby, tree[baby]])

for i in result[2:]:
    print(i)