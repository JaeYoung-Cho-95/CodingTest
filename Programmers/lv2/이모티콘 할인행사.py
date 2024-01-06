from itertools import product


def solution(users, emoticons):
    emoticons = sorted(emoticons, key=lambda x : x)
    answer = [0,0]

    for temp_percent in product([10,20,30,40], repeat=len(emoticons)):
        cnt = [0,0]
        for user_percent, user_asign in users:
            temp = 0
            for idx, percent in enumerate(temp_percent):
                if percent >= user_percent:
                    temp += int(emoticons[idx] * (100 - percent) / 100)
                
                if temp >= user_asign:
                    temp = 0
                    cnt[0] += 1
                    break
                        
            cnt[1] += temp
        
        if answer[0] < cnt [0]:
            answer[0] = cnt[0]
            answer[1] = cnt[1]
            
        elif answer[0] == cnt [0]:    
            if answer[1] <= cnt[1]:
                answer[1] = cnt[1]
            
    return answer


if __name__ == "__main__":
    # print(solution(users=[[40, 10000],[25, 10000]], emoticons=[7000, 9000]))
    print(solution([[40, 2900], [23, 10000], [11, 5200], [5, 5900], [40, 3100], [27, 9200], [32, 6900]],[1300, 1500, 1600, 4900]))
    