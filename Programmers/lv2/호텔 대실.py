def solution(book_time):
    from datetime import datetime, timedelta
    from collections import deque

    format = "%H:%M"
    book_time = sorted(book_time, key=lambda x: datetime.strptime(x[0], format))

    rooms = deque([])
    cnt = 0

    for book in book_time:
        st_time = datetime.strptime(book[0], format)
        ed_time = datetime.strptime(book[1], format) + timedelta(minutes=10)

        flag = True
        for index in range(len(rooms)):
            if rooms[index] <= st_time:
                rooms.remove(rooms[index])
                rooms.append(ed_time)
                flag = False
                break

        if flag:
            rooms.append(ed_time)
            cnt += 1

    return cnt


if __name__ == "__main__":
    print(solution([["00:01", "00:10"], ["00:19", "00:29"]]))
