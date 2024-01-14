def solution(storey):
    from collections import deque
    storey = deque([int(x) for x in str(storey)[::-1]])
    
    answer = 0
    while storey:
        temp = storey.popleft()
        
        if temp == 5 and storey:
            cnt = 0
            if storey[cnt] >= 5:
                storey[cnt] += 1
                while cnt < len(storey):
                    if storey[cnt] == 10:
                        storey[cnt] = 0
                        storey[cnt+1] += 1
                        cnt += 1
                    else:
                        break
            answer += temp
            
        elif temp >= 6:
            answer += (10 - temp)
            if storey:
                storey[0] += 1
            else:
                answer += 1
        else:
            answer += temp
        
    return answer

if __name__ == "__main__":
    print(solution(16))
    print(solution(2554))
    print(solution(1000000))
    print(solution(2999999))
    print(solution(5999999))
    print(solution(35))