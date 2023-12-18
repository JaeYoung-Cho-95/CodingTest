def solution(lottos, win_nums):
    min, max = 0,0
    for i in lottos:
        if i in win_nums:
            min += 1
            max += 1
        if i == 0:
            max += 1
            
    rank = [6,6,5,4,3,2,1]

    return [rank[max],rank[min]]