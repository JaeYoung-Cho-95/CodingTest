def solution(board):
    from copy import deepcopy
    board_copy = deepcopy(board)
    temp = [[0,1],[0,-1],[1,0],[-1,0],[1,1],[1,-1],[-1,1],[-1,-1]]
    
    for idx, i in enumerate(board):
        for jdx, j in enumerate(board[idx]):
            if j == 1:
                for move_i,move_j in temp:
                    temp_i = idx + move_i
                    temp_j = jdx + move_j
                    
                    if temp_i < 0 or temp_i >= len(board):
                        continue
                    if temp_j < 0 or temp_j >= len(board[0]):
                        continue
                    
                    board_copy[temp_i][temp_j] = 1
    
    cnt = 0
    for bd in board_copy:
        cnt += sum(bd)
        
    return len(board) * len(board[0]) - cnt