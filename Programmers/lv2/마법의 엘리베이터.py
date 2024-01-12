def solution(storey):
    from collections import deque
    storey = deque([x for x in str(storey)[::-1]])
    print(storey)
    
    answer = 0
    while storey:
        temp = int(storey.popleft())
        
        if temp >= 6:
            temp = 10 - temp + 1
            answer += temp
        else:
            answer += temp
        
    return answer

if __name__ == "__main__":
    print(solution(16))
    print(solution(2554))
    print(solution(24312304810))