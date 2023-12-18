def solution(keymap, targets):
    key_min_map = {}
    answer = []
    for key in keymap:
        for i,v in enumerate(key):
            try:
                if key_min_map[v] >= i+1:
                    key_min_map[v] = i+1
            except:
                key_min_map[v] = i+1

    for taget in targets:
        cnt = 0
        for value in taget:
            try:
                cnt += key_min_map[value]
            except:
                cnt = -1
                break
                
        answer.append(cnt)
    return answer