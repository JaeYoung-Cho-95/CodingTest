def bfs(start_point, end_point, maps, check_maps):
    from collections import deque

    need_visit = deque([start_point])
    check_maps[start_point[0]][start_point[1]] = 1

    temp = [[0, 1], [0, -1], [1, 0], [-1, 0]]

    while need_visit:
        i_idx, j_jdx = need_visit.popleft()

        for minus_i_idx, minus_j_jdx in temp:
            move_i_idx, move_j_jdx = i_idx + minus_i_idx, j_jdx + minus_j_jdx

            if move_i_idx < 0 or move_i_idx >= len(maps):
                continue

            if move_j_jdx < 0 or move_j_jdx >= len(maps[0]):
                continue

            if check_maps[move_i_idx][move_j_jdx] == False:
                check_maps[move_i_idx][move_j_jdx] = check_maps[i_idx][j_jdx] + 1
                need_visit.append([move_i_idx, move_j_jdx])

        if check_maps[end_point[0]][end_point[1]]:
            return check_maps[end_point[0]][end_point[1]] - 1


def solution(maps):
    from copy import deepcopy

    check_maps1 = [[False for _ in range(len(maps[0]))] for _ in range(len(maps))]

    for i_idx, i in enumerate(maps):
        for j_jdx, j in enumerate(i):
            if j == "S":
                start_point = [i_idx, j_jdx]
            if j == "L":
                middle_point = [i_idx, j_jdx]
            if j == "E":
                end_point = [i_idx, j_jdx]
            if j == "X":
                check_maps1[i_idx][j_jdx] = float("inf")

    check_maps2 = deepcopy(check_maps1)
    st_md = bfs(start_point, middle_point, maps, check_maps1)
    md_ed = bfs(middle_point, end_point, maps, check_maps2)

    if not st_md or not md_ed:
        return -1
    return st_md + md_ed


if __name__ == "__main__":
    print(solution(["SOOOL", "XXXXO", "OOOOO", "OXXXX", "OOOOE"]), 16)
    print(solution(["LOOXS", "OOOOX", "OOOOO", "OOOOO", "EOOOO"]), -1)
