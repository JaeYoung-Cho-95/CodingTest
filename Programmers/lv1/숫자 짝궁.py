def solution(X, Y):
    cnt_Y = {key: 0 for key in Y}
    for i in Y:
        cnt_Y[i] += 1

    answer = []
    for i in X:
        try:
            if cnt_Y[i] > 0:
                answer.append(str(i))
                cnt_Y[i] -= 1
        except:
            pass

    if len(answer) == 0:
        return "-1"

    answer = sorted(answer, reverse=True)
    if answer[0] == '0':
        return "0"
    
    answer = "".join(answer)
    return answer


if __name__ == "__main__":
    # print(solution("100", "2345"))
    print(solution("100", "203045"))
    print(solution("2987654", "1200000"))
