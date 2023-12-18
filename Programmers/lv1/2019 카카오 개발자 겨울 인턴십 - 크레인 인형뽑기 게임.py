def solution(boards, moves):
    
    answer = 0
    
    x = list(map(lambda y:y-1,moves))
    
    temp = [0]
    
    for i in x:
        for board in boards:
            if board[i] != 0:
                temp.append(board[i])
                board[i] = 0
                if temp[-1] == temp[-2]:
                    temp.pop()
                    temp.pop()
                    answer += 2
                break

    return answer