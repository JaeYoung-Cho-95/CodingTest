def solution(p):
    
    def r_cnt(inputs):
        # input 값이 빈 문자열인 경우 빈 문자열 반환
        if inputs == "":
            return ""
        
        # 균형잡힌 문자열 끊어주기
        left_cnt = 0
        right_cnt = 0

        for i in inputs:
            if i == '(':
                left_cnt += 1
            elif i == ')':
                right_cnt += 1
                
            u = ""
            v = ""
            
            # 균형잡힌 문자열이라면
            if left_cnt == right_cnt:
                u += inputs[:left_cnt+right_cnt]
                v += inputs[left_cnt+right_cnt:]
                
                # 괄호의 개수가 같기 때문에 처음과 끝이 ( ) 으로 돼 있다면 == 올바른 문자열
                if u[0] == '(' and u[-1] == ')':
                    return u + r_cnt(v)
                
                # 올바른 문자열이 아니라면
                else:
                    # 처음과 끝에 ( ) 더해주고
                    temp = '('
                    temp += r_cnt(v)
                    temp += ')'                            
                    
                    # '(' 가 출력되면 ')' 로 바꿈,  ')' 가 출력되면 '(' 로 바꿈
                    if len(u) > 2:
                        for i in u[1:-1]:
                            if i == '(':
                                temp += ')'
                            else:
                                temp += '('
                                
                    return temp

    answer = r_cnt(p)
    
    return answer