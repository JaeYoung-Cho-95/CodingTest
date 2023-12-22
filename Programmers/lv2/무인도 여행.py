def dfs(st_i_idx, st_j_idx, check_maps):
    from collections import deque

    temp = [[0, 1], [0, -1], [1, 0], [-1, 0]]
    need_visit = deque([[st_i_idx, st_j_idx]])
    cnt = int(check_maps[st_i_idx][st_j_idx])
    check_maps[st_i_idx][st_j_idx] = False

    while need_visit:
        st_i_idx, st_j_idx = need_visit.popleft()

        for i_plus, j_plus in temp:
            i_idx = st_i_idx + i_plus
            j_jdx = st_j_idx + j_plus

            if i_idx >= len(check_maps) or i_idx < 0:
                continue
            if j_jdx >= len(check_maps[0]) or j_jdx < 0:
                continue

            if check_maps[i_idx][j_jdx]:
                cnt += int(check_maps[i_idx][j_jdx])
                check_maps[i_idx][j_jdx] = False
                need_visit.extend([[i_idx, j_jdx]])

    return cnt, check_maps


def solution(maps):
    check_maps = [[x if x != "X" else False for x in i] for i in maps]

    answer = []
    for i_idx in range(len(maps)):
        for j_idx in range(len(maps[0])):
            if check_maps[i_idx][j_idx]:
                cnt, check_maps = dfs(i_idx, j_idx, check_maps)
                answer.append(cnt)
    if answer:
        return sorted(answer)
    return [-1]


if __name__ == "__main__":
    print(solution(["X591X", "X1X5X", "X231X", "1XXX1"]))
