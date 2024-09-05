from collections import deque


def solution(ingredient):
    answer = 0
    x = deque()
    for i in ingredient:
        x.append(i)
        if len(x) >= 4 and x[-4] == 1 and x[-3] == 2 and x[-2] == 3 and x[-1] == 1:
            answer += 1
            [x.pop() for _ in range(4)]
    return answer
