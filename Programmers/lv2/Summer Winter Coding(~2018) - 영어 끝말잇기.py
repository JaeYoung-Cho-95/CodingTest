import math

def solution(n,words):
    cnt = 0
    check = True
    check_word = {}

    while True:
        check_word[words[cnt]] = True

        if words[cnt][-1] != words[cnt+1][0]:
            break

        try:
            if check_word[words[cnt+1]] == True:
                break
        except:
            pass

        cnt += 1
        if cnt >= len(words)-1:
            check = False
            break

    if not check:
        return [0,0]
    else:
        cnt += 2
        result = [n if cnt % n  == 0 else cnt % n, math.ceil(cnt/n)]
        return result