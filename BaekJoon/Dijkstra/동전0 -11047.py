from heapq import heappush, heappop
from sys import stdin
node, edge = list(map(int, stdin.readline().split()))
start_node = int(input())
tree = {x:{} for x in range(1,node+1)}
for _ in range(edge):
    st_node, ed_node, weight = list(map(int, stdin.readline().split()))
    try:
        if tree[st_node][ed_node] > weight:
            tree[st_node][ed_node] = weight
    except:
        tree[st_node][ed_node] = weight


distance = [float("inf") for i in range(node+1)]
distance[start_node] = 0

queue = []

heappush(queue, [distance[start_node],start_node])

while queue:
    current_distance, current_node = heappop(queue)

    if distance[current_node] < current_distance:
        continue
    
    for next_node, weight in tree[current_node].items():
        next_distance = current_distance + weight

        if distance[next_node] > next_distance:
            distance[next_node] = next_distance
            heappush(queue, [next_distance, next_node])

for i in distance[1:]:
    if float("inf") == i:
        print("INF")
    else:
        print(i)