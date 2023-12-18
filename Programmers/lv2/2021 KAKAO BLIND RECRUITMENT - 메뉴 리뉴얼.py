def solution(orders, course):
    from itertools import combinations
    result = []
    for num in course:
        _dict = {}
        for menu in orders:
            menu = ''.join(sorted(menu))
            for i in list(combinations(menu,num)):
                if i in _dict:
                    _dict[i] += 1
                else:
                    _dict[i] = 1
        sort_dict = sorted(_dict.items(), key=lambda x : x[1], reverse=True)
        
        if len(sort_dict) == 0:
            continue
        
        if sort_dict[0][1] >= 2:
            result.append(''.join(sort_dict[0][0]))            
            if len(sort_dict) >= 2:
                for i in range(1,len(sort_dict)):
                    if sort_dict[0][1] == sort_dict[i][1]:
                        result.append(''.join(sort_dict[i][0]))
                    else:
                        break
    result.sort()
    
    return result