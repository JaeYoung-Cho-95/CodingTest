def solution(board, h, w):
    temp = [[0,1],[0,-1],[1,0],[-1,0]]
    answer = 0
    for h_minus, w_minus in temp:
        new_h = h-h_minus
        new_w = w-w_minus
        
        if new_h < 0 or new_h >= len(board):
            continue
        
        if new_w < 0 or new_w >= len(board[0]):
            continue
        
        if board[h][w] == board[new_h][new_w]:
            answer += 1
            
    return answer