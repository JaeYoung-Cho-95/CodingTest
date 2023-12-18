def check_bingo(bingo, idx_i, idx_j):
    directs = [[[-1,0],[-2,0]], [[1,0],[2,0]], [[1,0],[-1,0]],[[0,1],[0,2]], [[0,-1],[0,-2]], [[0,-1],[0,1]], [[1,1],[2,2]], [[-1,1],[-2,2]]]

    for direct in directs:
        for idx, (minus_i, minus_j) in enumerate(direct):
            temp_i = idx_i - minus_i
            temp_j = idx_j - minus_j
            
            if temp_i > 2 or temp_i < 0:
                break
            if temp_j > 2 or temp_j < 0:
                break
            if bingo[temp_i][temp_j] != bingo[idx_i][idx_j]:
                break
            if idx == 1:
                return bingo[temp_i][temp_j], True
    return None, False
    
def solution(board):
    cnt_O, cnt_X = 0, 0
    bingo_check_dict = {
        "O" : False,
        "X" : False
    }
    
    for idx_i, i in enumerate(board):
        for idx_j, j in enumerate(i):
            if j == "O":
                cnt_O += 1
            if j == "X":
                cnt_X += 1
            if j == "O" or j == "X":
                value, flag = check_bingo(board, idx_i, idx_j)
                
                if flag:
                    bingo_check_dict[value] = flag

    if bingo_check_dict["O"] and bingo_check_dict["X"]:
        return 0
    if bingo_check_dict["O"] and not (cnt_O == cnt_X + 1):
        return 0
    if bingo_check_dict["X"] and not (cnt_O == cnt_X):
        return 0
    if (cnt_O == cnt_X + 1) or (cnt_O == cnt_X):
        return 1
    else:
        return 0