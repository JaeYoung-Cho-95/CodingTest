def solution(str1, str2):
    str1 = [str1[x:x+2].upper() for x in range(len(str1)-1)]
    str2 = [str2[x:x+2].upper() for x in range(len(str2)-1)]
    
    for i in str1.copy():
        for j in i:
            if ord(j) < 65 or ord(j) > 90:
                str1.remove(i)
                break

    for i in str2.copy():
        for j in i:
            if ord(j) < 65 or ord(j) > 90:
                str2.remove(i)
                break

    if len(str1) == 0 and len(str2) == 0:
        return int(1 * 65536)        
    
    str2_copy = str2.copy()
    
    # intersection
    intersection = []
    for i in str1:
        if i in str2_copy:
            str2_copy.remove(i)
            intersection.append(i)
                
    # union
    union = []
    for i in str1.copy():
        if i in str2:
            str2.remove(i)
        
        union.append(i)
        str1.remove(i)
        
    for i in str2:
        union.append(i)

    
    return int(len(intersection) / len(union) * 65536)