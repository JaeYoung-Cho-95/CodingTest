def solution(friends, gifts):
    받은거 = {}
    준거 = {}
    선물지수 = {}
    다음달예상 = {}
    
    for name in friends:
        받은거[name] = {}
        준거[name] = {}
        
        선물지수[name] = {}
        다음달예상[name] = 0
        
        for an_name in friends:
            if an_name != name:
                받은거[name][an_name] = 0
                준거[name][an_name] = 0
        
    
    for i in gifts:
        a,b = i.split(" ")[0], i.split(" ")[1]
        try:
            받은거[b][a] += 1
            준거[a][b] += 1
        except:
            받은거[b][a] = 1
            준거[a][b] = 1
    
    for name in friends:
        받은수 = sum(받은거[name].values())
        준수 = sum(준거[name].values())
        선물지수[name] = 준수 - 받은수
    
    for i in range(len(friends)):
        name = friends[i]
        for j in range(i+1, len(friends)):
            an_name = friends[j]
            if 준거[name][an_name] > 준거[an_name][name]:
                다음달예상[name] += 1
            elif 준거[name][an_name] < 준거[an_name][name]:
                다음달예상[an_name] += 1
            else:
                if 선물지수[name] < 선물지수[an_name]:
                    다음달예상[an_name] += 1
                elif 선물지수[name] > 선물지수[an_name]:
                    다음달예상[name] += 1

    return max(다음달예상.values())