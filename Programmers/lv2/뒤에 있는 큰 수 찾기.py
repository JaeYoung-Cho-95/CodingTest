def solution(numbers):
    answer = [-1] * len(numbers)
    stack = []

    for i, number in enumerate(numbers):
        while stack and numbers[stack[-1]] < number:
            answer[stack.pop()] = number
        stack.append(i)
    return answer


if __name__ == "__main__":
    print(solution([2, 3, 3, 5]))
    print(solution([9, 1, 5, 3, 6, 2]))
