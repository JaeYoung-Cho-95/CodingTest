def solution(id_list, report, k):
    dict_id = {}
    dict_idx_id = {}
    cnt = 0

    for i in id_list: 
        dict_id[i] = []
        dict_idx_id[i] = cnt
        cnt += 1
    
    for i in report:
        i = i.split(' ')
        if i[1] not in dict_id[i[0]]:
            dict_id[i[0]].append(i[1])
    
    answer = [0 for _ in range(len(id_list))]
    for id in id_list:
        check = [0 for _ in range(len(id_list))]
        cnt = 0
        for i, v in dict_id.items():
            if id in v:
                cnt += 1
                check[dict_idx_id[i]] += 1
        
        if cnt >= k:
            for i in range(len(answer)):
                answer[i] += check[i]

    return answer