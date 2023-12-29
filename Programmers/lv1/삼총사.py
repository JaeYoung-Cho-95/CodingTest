def solution(number):
    i = 0
    j = 1
    t = 2

    answer = 0
    while True:
        temp = number[i] + number[j] + number[t]
        if not temp:
            answer += 1

        t += 1

        if i == len(number) - 3:
            break

        if t >= len(number):
            j += 1
            t = j + 1

        if j >= len(number) - 1:
            i += 1
            j = i + 1
            t = j + 1

    return answer


if __name__ == "__main__":
    print(solution([-2, 3, 0, 2, -5]))
