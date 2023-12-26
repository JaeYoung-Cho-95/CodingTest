def solution(numbers):
    answer = [-1 for _ in range(len(numbers))]
    stack = []

    for idx, value in enumerate(numbers):
        while stack:
            if numbers[stack[-1]] < value:
                answer[stack.pop()] = value
            else:
                break
        stack.append(idx)

    return answer


if __name__ == "__main__":
    print(solution([2, 3, 3, 5]))
    print(solution([9, 1, 5, 3, 6, 2]))
