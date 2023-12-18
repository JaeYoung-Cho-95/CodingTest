# 입력받기
n = int(input())
stack, temp = list(map(int,input().split())), []
check = True


# stack 에서 재귀적으로 가장 앞에 값이 있는지 찾기
# 만약, stack 의 가장 앞에 있는 값이 원하는 값이면 탈출
# 또는 stack 의 길이가 0이면 탈출
# 둘 다 아니면 재귀
def stack_recursive(stack, temp, check):
    if len(stack) == 0:
        return stack, temp, False
        
    if stack[0] == i:
        stack.pop(0)
        return stack, temp, True
    else:
        temp.append(stack.pop(0))
        return stack_recursive(stack,temp, check)

# 1부터 순차적으로 값 찾기
for i in range(1,n+1):
    if len(temp) > 0 and temp[-1] == i:
        temp.pop()
    else:
        stack, temp, check = stack_recursive(stack,temp, check)
		
    if not check: 
        print("Sad")
        break
    elif i == n: 
        print("Nice")