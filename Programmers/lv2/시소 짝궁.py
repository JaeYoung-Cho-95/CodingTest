def solution(weights):
    weights = sorted(weights)
    weights_count = {weight: 0 for weight in weights}
    for weight in weights:
        weights_count[weight] += 1

    answer = 0
    for weight in weights:
        if weights_count[weight] >= 2:
            weights_count[weight] -= 1
            answer += weights_count[weight]

        temp = [weight * 2 / 1, weight * 3 / 2, weight * 4 / 3]

        for tmp in temp:
            try:
                if weights_count[tmp] >= 1:
                    answer += weights_count[tmp]
            except:
                pass

    return answer


if __name__ == "__main__":
    print(solution([100, 180, 360, 100, 270]))

    print(solution([100, 100, 100, 150, 150, 200, 300]))
