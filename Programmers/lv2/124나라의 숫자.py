def solution(n):
    temp = [1,2,4]
    a,b = divmod(n-1,3)
    res = str(temp[b])
    if a == 0:
        return res
    elif a >= 1 and a <= 3:
        res = str(temp[a-1]) + res
        return res
    while a > 3:
        if a % 3 == 0:
            _,b = divmod(a,3)
            res = str(temp[b-1]) + res
            a,b = divmod(a-1,3)
        else:
            a,b = divmod(a,3)
            res = str(temp[b-1]) + res
    return str(temp[a-1]) + res