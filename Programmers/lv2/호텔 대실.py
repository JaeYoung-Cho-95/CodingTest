def solution(book_time):
    from datetime import datetime, timedelta

    book_time = sorted(book_time, key=lambda x: datetime.strptime(x[0], "%H:%M"))

    available_times = []

    for st_time, ed_time in book_time:
        start = datetime.strptime(st_time, "%H:%M")
        end = datetime.strptime(ed_time, "%H:%M") + timedelta(minutes=10)

        flag = False
        for i in available_times:
            if i <= start:
                i = end
                flag = True
                break

        if not flag:
            available_times.append(end)

    return len(available_times)


if __name__ == "__main__":
    print(
        solution(
            [
                ["09:10", "10:10"],
                ["09:10", "10:10"],
                ["10:20", "12:20"],
                ["10:20", "12:20"],
            ]
        )
    )

    # 2
    print(solution([["00:01", "00:10"], ["00:19", "00:29"]]))

    # 2
    print(solution([["08:00", "08:30"], ["08:00", "13:00"], ["12:30", "13:30"]]))

    # 1
    print(solution([["16:00", "16:10"], ["16:20", "16:30"], ["16:40", "16:50"]]))

    # 2
    print(solution([["15:00", "17:00"], ["15:00", "17:00"]]))

    # 1
    print(solution([["09:10", "10:10"], ["10:20", "12:20"], ["12:30", "13:20"]]))

    # 1
    print(solution([["10:00", "10:10"]]))
