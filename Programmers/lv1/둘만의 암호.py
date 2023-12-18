def solution(s, skip, index):
    answer = ""
    for al in s:
        idx_num = index
        num_al = ord(al)
        
        while idx_num > 0:
            num_al += 1
            
            if num_al > 122:
                num_al -= 26
            
            if chr(num_al) in skip:
                continue
            
            idx_num -= 1
            
        answer += chr(num_al)
    return answer