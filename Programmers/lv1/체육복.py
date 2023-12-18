def solution(n, lost, reserve):
    n = n - len(lost)
    for i in reserve[:]:
        if i in lost:
            reserve.remove(i)
            lost.remove(i)
            n += 1

    temp = []
    for i in reserve[:]:
        if i-1 in lost and i+1 in lost:
            temp.append(i)
        elif i-1 in lost:
            lost.remove(i-1)
            n += 1
        elif i+1 in lost:
            lost.remove(i+1)
            n += 1

    for i in temp:
        if i-1 in lost:
            lost.remove(i-1)
            n += 1
        elif i+1 in lost:
            lost.remove(i+1)
            n += 1

    return n