from collections import deque

num, index_num = map(int,input().split())
data_list = deque([i for i in range(1,num+1)])

result = []
cnt = 1
while True:
    temp = data_list.popleft()

    if cnt % index_num == 0:
        result.append(temp)
    else:
        data_list.append(temp)

    cnt += 1

    if len(data_list) == 0:
        break

result = str(result)
result = result.replace('[', '<')
result = result.replace(']', '>')
print(result)