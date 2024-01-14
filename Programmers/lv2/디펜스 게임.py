def solution(n, k, enemy):
    from collections import deque
    from heapq import heappop, heappush
    enemy = deque(enemy)
    heap = []
    cnt, answer = 0, 0
    
    while enemy:
        temp = enemy.popleft()
        heappush(heap, [-1 * temp, temp])
        cnt += temp
        
        if cnt > n and k >= 1:
            x = heappop(heap)
            cnt -= x[1]
            k -= 1
        
        if cnt > n and k <= 0:
            break
            
        answer += 1

    return answer
    
if __name__ == "__main__":
    print(solution(7,3,[4,2,4,5,3,3,1]))
    print(solution(7,3,[4,2,4,5,3,3,1]))
    print(solution(10, 1, [5, 5, 5, 5, 5]))
    print(solution(10, 2, [5, 5, 5, 5, 5]))
    print(solution(5,2,[99,1,99]))
    print(solution(2,4,[3,3,3,3]))