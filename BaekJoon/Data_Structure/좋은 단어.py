from collections import deque
n = int(input())
cnt = 0
for _ in range(n):
    temp = input()
    stack_list = deque()
    for i in temp:
        stack_list.append(i)        
        if len(stack_list) > 1 and stack_list[-2] == stack_list[-1]:
            stack_list.pop()
            stack_list.pop()
    if len(stack_list) == 0:
       cnt += 1
print(cnt) 