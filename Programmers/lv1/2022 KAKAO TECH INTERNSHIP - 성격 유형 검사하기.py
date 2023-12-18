def solution(survey, choices):
    _length = len(survey)
    answer = ""
    
    result = {"R":0, "T":0, "C":0, "F":0, "J":0, "M":0, "A":0, "N":0}
    score = {1:3,2:2,3:1,5:1,6:2,7:3}
    x = [["R","T"],["C","F"], ["J","M"],["A","N"]]
    
    for i in range(_length):
        if choices[i] > 4:
            result[survey[i][1]] += score[choices[i]]
        elif choices[i] < 4:
            result[survey[i][0]] += score[choices[i]]

    for i in x:
        if result[i[0]] > result[i[1]]:
            answer += i[0]
        elif result[i[0]] < result[i[1]]:
            answer += i[1]
        else:
            answer += i[0]
    
    return answer