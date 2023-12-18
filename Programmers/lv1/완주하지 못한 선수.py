def solution(participant, completion):
    participant= sorted(participant)
    completion = sorted(completion)
    try:
        for i in range(len(participant)):
            if participant[i] != completion[i]:
                return participant[i]
    except:
        return participant[-1]