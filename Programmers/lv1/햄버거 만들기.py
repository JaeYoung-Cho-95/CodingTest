def solution(ingredient):
    x = [1,2,3,1]
    answer,idx = 0,0
    while len(ingredient) > idx+3:
        if ingredient[idx:idx+4] == x:
            del ingredient[idx:idx+4]
            # ingredient = ingredient[0:idx] + ingredient[idx+4:]
            idx -= 2
            answer += 1
        else:
            idx += 1    
    return answer