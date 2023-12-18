def solution(now):
    from datetime import time, datetime
    
    def cal_term(a,b,c,d):
        x =  datetime.strptime(f"{a}:{b}", "%H:%M") - datetime.strptime(f"{c}:{d}", "%H:%M")
        return int(x.seconds/60)

    def make_time(hour,minute):
        date = 1
        while minute >= 60:
            hour += 1
            minute -= 60

        if hour >= 24:
            hour -= 24
            date = 2

        return date, hour, minute
    
    future = []
    now  = sorted(now, key= lambda x: x[1])
    finish = []
    
    for idx in range(len(now)-1):
        comp1_hour,comp1_minute = list(map(int,now[idx][1].split(":")))
        comp2_hour,comp2_minute  = list(map(int,now[idx+1][1].split(":")))

        comp1_term = int(now[idx][2])
        comp2_term = int(now[idx+1][2])

        date, new_comp1_hour, new_comp1_minute = make_time(comp1_hour, comp1_minute + comp1_term)
        if datetime.strptime(f"{date}.{new_comp1_hour}:{new_comp1_minute}","%d.%H:%M") <= datetime.strptime(f"1.{comp2_hour}:{comp2_minute}","%d.%H:%M"):
        # if time(new_comp1_hour, new_comp1_minute) <= time(comp2_hour, comp2_minute):
            finish.append(now[idx][0])
            remain_term = cal_term(comp2_hour,comp2_minute, new_comp1_hour, new_comp1_minute)
            
            while (len(future) > 0) and (remain_term > 0):
                temp = future.pop()
                if temp[1] <= remain_term:
                    remain_term -= temp[1]            
                    finish.append(temp[0])
                else:
                    temp[1] -= remain_term
                    future.append(temp)
                    break
        
        else:
            new_term = comp1_term - cal_term(comp2_hour,comp2_minute,comp1_hour,comp1_minute)
            future.append([now[idx][0], new_term])

    finish.append(now[-1][0])
    
    for i in future[::-1]:
        finish.append(i[0])

    return finish