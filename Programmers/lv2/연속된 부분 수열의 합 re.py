def make_answer(a,b):
    origin_x, origin_y = a
    comp_x, comp_y = b
    
    temp_a = origin_y - origin_x
    temp_b = comp_y - comp_x
    
    if temp_a == temp_b:
        if origin_x < comp_x:
            return [origin_x, origin_y]
        else:
            return [comp_x, comp_y]
    if temp_a > temp_b:
        return [comp_x, comp_y]
    
    return [origin_x, origin_y]

def make_idx(sequence, k):
    for idx, value in enumerate(sequence):
        if value == k:
            return idx
        elif value > k:
            break
    
    if value > k:
        return idx - 1
    else:
        return idx

def solution(sequence, k):
    from copy import deepcopy
    
    st_idx = make_idx(sequence,k)
    std_idx = deepcopy(st_idx)
    
    answer = []
    temp = 0
    while True:
        temp += sequence[std_idx]
        
        if temp > k:
            temp = 0
            st_idx -= 1
            std_idx = deepcopy(st_idx)
        else:
            if temp == k:
                try:
                    answer = make_answer(answer, [std_idx, st_idx])
                except:
                    answer = [std_idx, st_idx]
            std_idx -= 1
        
        if std_idx < 0:
            temp = 0
            st_idx -= 1
            std_idx = deepcopy(st_idx)
        if st_idx < 0:
            break

    return answer
    
if __name__ == "__main__":
    test_case = [1] + [2 for _ in range(1000000)] + [10000000]
    # print(solution(test_case, 10000001))
    print(solution([1, 1, 1, 2, 3, 4, 5], 5))
    print(solution([2, 2, 2, 2, 2],6))
    print(solution([1, 2, 3, 4, 5],7))