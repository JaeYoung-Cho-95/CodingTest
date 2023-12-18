def solution(n, arr1, arr2):
    answer = []
    arr1 = [bin(x)[2:] for x in arr1]
    arr2 = [bin(x)[2:] for x in arr2]
    
    for i in range(n):
        if len(arr1[i]) <= n:
            arr1[i] = (n-len(arr1[i])) * '0' + arr1[i]
        if len(arr2[i]) <= n:
            arr2[i] = (n-len(arr2[i])) * '0' + arr2[i]
        temp = ''
        for j in range(n):
            if int(arr1[i][j]) + int(arr2[i][j]) == 0:
                temp += ' '
            else:
                temp += '#'
        answer.append(temp)
    return answer