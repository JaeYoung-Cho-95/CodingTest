def solution(fees, records):
    def cal(fees,time):
        import math
        if time < fees[0]:
            return fees[1]
        else:
            return fees[1] + math.ceil((time - fees[0])/fees[2]) * fees[3]

    def cal_time(in_time, out_time):
        in_H, in_M = map(int,in_time.split(':'))
        out_H, out_M = map(int,out_time.split(':'))

        return (out_H - in_H) * 60 + (out_M - in_M)
    
    inout_record = {}
    in_record = []

    for i in records:
        i = i.split(' ')
        if i[2] == 'IN':
            in_record.append([i[1],i[0]])

            if i[1] not in inout_record:
                inout_record[i[1]] = 0
                
        elif i[2] == 'OUT':
            for j in in_record:
                if j[0] == i[1]:
                    plus_time = cal_time(j[1],i[0])
                    # fee = cal(fees,j[1],i[0])
                    inout_record[i[1]] += plus_time
                    in_record.remove([j[0],j[1]])
                    break
    
    if in_record:
        for i in in_record:
            plus_time = cal_time(i[1],'23:59')
            if i[0] in inout_record:
                inout_record[i[0]] += plus_time
            else:
                print('qqq')
                print(i[0])
                print(inout_record)
                inout_record[i[0]] = plus_time

    inout_record = sorted(inout_record.items())
    answer = []
    for i in inout_record:
        answer.append(cal(fees,i[1]))
    return answer