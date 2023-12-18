def solution(s):
    def start(s,interval):
        if s[0:interval] != s[interval:2*interval]:
            return s[0:interval] + start(s[interval:],interval)
        temp = ""
        check_point = 0
        cnt = 1
        while True:
            if s[check_point:check_point+interval] == s[check_point+interval:check_point+(2*interval)]:
                cnt += 1
                check_point += interval
                if s[check_point:check_point+interval] == "":
                    return ""
            else:
                temp += "{}{}".format(cnt,s[check_point:check_point+interval])
                break
        return temp + start(s[check_point+interval:],interval)        
    
    if len(s) <= 1:
        return len(s)
    
    result = []
    for i in range(1,int(len(s)/2)+1):
        result.append(len(start(s,i)))

    return sorted(result)[0]