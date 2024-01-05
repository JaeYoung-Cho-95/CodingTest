def find_first_point(n,deliveries, pickups):
    for i in range(n, -1, -1):
        if deliveries[i] >= 1:
            break

    for j in range(n, -1, -1):
        if pickups[j] >= 1:
            break

    if i > j:
        return i
    return j
        

def solution(cap, n, deliveries, pickups):
    from copy import deepcopy
    deli_n = deepcopy(n)
    pick_n = deepcopy(n)
    
    deliveries = [0] + deliveries
    pickups = [0] + pickups
    
    cnt = 2 * find_first_point(n,deliveries, pickups)

    while True:
        temp = 0
        while deli_n > 0:
            if deliveries[deli_n] + temp <= cap:
                temp += deliveries[deli_n]
                deliveries[deli_n] = 0
                deli_n -= 1
            else:
                deliveries[deli_n] -= (cap - temp)
                break
        
        temp = 0
        while pick_n > 0:
            if pickups[pick_n] + temp <= cap:
                temp += pickups[pick_n]
                pickups[pick_n] = 0
                pick_n -= 1
            else:
                pickups[pick_n] -= (cap - temp)
                break
        
        if deli_n >= pick_n:
            cnt += (2 * deli_n)
        else:
            cnt += (2 * pick_n)
            
        if deli_n == 0 and pick_n == 0:
            break

    return cnt

if __name__ == '__main__':
    # 16
    print(solution(4,5,[1, 0, 3, 1, 2],[0, 3, 0, 4, 0]))
    
    # 30
    print(solution(2,7,[1, 0, 2, 0, 1, 0, 2],[0, 2, 0, 1, 0, 2, 0]))
    
    # 3002
    print(solution(1, 5, [300, 0, 1, 0, 0], [0, 0, 0, 0, 300]))
    
    # 8
    print(solution( 2, 2, [0, 0], [0, 4]))
    
    # 0
    print(solution( 2, 2, [0, 0], [0, 0]))
    
    # 8
    print(solution(3, 2, [2, 4], [4, 2]))