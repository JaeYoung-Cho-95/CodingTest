def check_pickups(cap, pickups, len_p):
    cnt = 0
    while True:
        if pickups[len_p] > cap:
            cnt += cap
            pickups[len_p] -= cap 
            break
        
        else:
            cnt += pickups[len_p]
            pickups[len_p] = 0
            
            
        
def solution(cap, n, deliveries, pickups):
    from copy import deepcopy
    cnt = 0
    len_d = deepcopy(n)
    len_p = deepcopy(n)
    
    while True:
        if deliveries[len_d] > 0:        
            if deliveries[len_d] >= cap:
                pass
            elif deliveries[len_d] < cap:
                pass
        elif deliveries[len_d] < 0:
            
    return cnt