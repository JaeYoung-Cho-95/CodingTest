def solution(x, y, n):
    from collections import deque

    need_visit = deque([])
    already_visit = [False for _ in range(y + 1)]

    need_visit.append([x, 0])

    while need_visit:
        temp_x, distance = need_visit.popleft()

        if already_visit[temp_x]:
            continue
        
        already_visit[temp_x] = True

        if temp_x == y:
            return distance
        else:
            temp = list({temp_x * 2, temp_x * 3, temp_x + n})

            for i in temp:
                if i > y:
                    continue
                if not already_visit[i]:
                    need_visit.append([i, distance + 1])
    return -1



if __name__ == "__main__":
    print(solution(10, 40, 5))
    print(solution(10, 40, 30))
    print(solution(2, 5, 4))
