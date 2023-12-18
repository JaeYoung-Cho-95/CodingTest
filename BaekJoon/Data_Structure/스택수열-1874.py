from sys import stdin

# 입력 변수의 개수를 나타내는 N 할당
N = int(stdin.readline().rstrip())

# Stack 자료구조 list로 만들어놓기
data_stack = []
index_stack = 1

# '+' 와 '-' 를 담아놓을 list 만들어놓기
result = []

# 만약, 잘못된 수열이라면 False로 만들 수 있는 Boolean type 변수 할당
check = True

# N 만큼 반복문
for i in range(N):
		# x 입력받기
    x = int(stdin.readline().rstrip())

		# 만약, x 가 index_stack 보다 같거나 크다면
    if x >= index_stack:
				# index_stack 부터 x 까지 data_stack list 에 append 해주고 그만큼 '+' 출력
        for i in range(index_stack, x+1):
            data_stack.append(i)
            result.append('+')
        
				# data_stack list 의 마지막은 출력할 것이니 바로 삭제
        del data_stack[-1]
        result.append('-')
				
				# 다음에 추가할 데이터는 x+1 부터 시작
        index_stack = x + 1

		# 만약 x가 index_stack 보다 작다면        
    elif x < index_stack:
				# data_stack list 의 마지막이 x 가 아니라면 stack 구조상 출력이 불가능하다.
        if data_stack[-1] != x:
            check = False
            break
				# data_stack list 의 마지막이 x 라면, result 에 '-' append 하고 data_stack list의 마지막 삭제
        else:
            result.append('-')
            del data_stack[-1]
            
if check:
    for i in result:
        print(i)
else:
    print('NO')