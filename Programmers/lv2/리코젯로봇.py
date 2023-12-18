def make_need_visit(board, already_visit, start_point):
    len_i, len_j = len(board), len(board[0])
    i_idx, j_idx, distance = start_point
    temp = [[1,0],[0,1],[-1,0],[0,-1]]
    need_visit = []
    
    for i_minus, j_minus in temp:
        new_i_idx = i_idx
        new_j_idx = j_idx
        while True:            
            new_i_idx -= i_minus
            new_j_idx -= j_minus
            
            if new_i_idx < 0:
                new_i_idx = 0
                break
            elif new_i_idx > len_i-1:
                new_i_idx = len_i-1
                break
            if new_j_idx < 0:
                new_j_idx = 0
                break
            elif new_j_idx > len_j-1:
                new_j_idx = len_j-1
                break
            if board[new_i_idx][new_j_idx] == "D":
                new_i_idx = new_i_idx + i_minus
                new_j_idx = new_j_idx + j_minus
                break
        
        if not already_visit[new_i_idx][new_j_idx]:
            need_visit.append([new_i_idx, new_j_idx, distance+1])

    return need_visit
    
def solution(board):
    from collections import deque
    
    answer = 0
    
    for i_idx, i in enumerate(board):
        for j_idx, j in enumerate(i):
            if j == "R":
                start_point = [i_idx, j_idx, 1]
            if j == "G":
                end_i_idx, end_j_idx = i_idx, j_idx
                
    need_visit = deque([start_point])
    already_visit = [[False for _ in range(len(board[0]))] for _ in range(len(board))]
    start_i_idx, start_j_idx, distacne = start_point
    
    while need_visit:
        start_i_idx, start_j_idx, distance = need_visit.popleft()
        
        if (start_i_idx == end_i_idx) and (start_j_idx == end_j_idx):
            answer = distance
            break

        if not already_visit[start_i_idx][start_j_idx]:
            already_visit[start_i_idx][start_j_idx] = distacne
            x = make_need_visit(board, already_visit,[start_i_idx, start_j_idx, distance])
            need_visit.extend(x)
    
    if not answer:
        return -1
    return answer-1