def solution(picks, minerals):
    pick_dict = {"diamond":picks[0], "iron":picks[1], "stone":picks[2]}
    
    if sum(pick_dict.values()) * 5 < len(minerals):
        minerals = minerals[:sum(pick_dict.values())*5]
        
    diaomond_pick = {"diamond":1,"iron":1,"stone":1}
    iron_pick = {"diamond":5,"iron":1,"stone":1}
    stone_pick = {"diamond":25,"iron":5,"stone":1}

    weight_dict = {"diamond":30, "iron":5, "stone":1}

    answer = []
    if len(minerals) % 5 == 0:
        x = int(len(minerals) / 5)
    else:
        x = int(len(minerals) / 5) + 1
        
    for i in range(x):
        weight = 0
        if i == x-1:
            temp = minerals[i*5:]
        else:
            temp = minerals[i*5:(i+1)*5]
            
        for j in temp:
            weight += weight_dict[j]
        answer.append([weight] + temp)
    
    answer = sorted(answer, key=lambda x: -x[0])

    cnt = 0
    for i in answer:
        if pick_dict["diamond"] > 0:
            pick = diaomond_pick
            pick_dict["diamond"] -= 1
        elif pick_dict["iron"] > 0:
            pick = iron_pick
            pick_dict["iron"] -= 1
        elif pick_dict["stone"] > 0:
            pick = stone_pick
            pick_dict["stone"] -= 1
        else:
            break

        for j in i[1:]:
            cnt += pick[j]
    
    return cnt