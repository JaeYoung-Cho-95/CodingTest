def solution(s):
    temp = {"x" : 0, 
           "y" : 0}
    
    cnt = 1
    for idx, i in enumerate(s):
        if temp["x"] == 0 and temp["y"] == 0:
            a = i
            temp["x"] += 1
            continue
        
        if i == a:
            temp["x"] += 1
        else:
            temp["y"] += 1
        
        if (temp["x"] == temp["y"]) and (idx != len(s)-1):
            cnt += 1
            temp["x"] = 0
            temp["y"] = 0
    
    return cnt