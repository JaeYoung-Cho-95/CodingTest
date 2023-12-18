def solution(places):
    # 5개의 대기실 순서대로 반환
    result = []
    for i in places:
        temp = True
        # 대기실 안에 행별로 출력
        for w in range(len(i)):
            # 행 중에 열별로 출력
            for h in range(len(i[w])):
                # 만약 'P' 사람이 보인다면
                if i[w][h] == 'P':
                    # 상하좌우
                    if h-1 >= 0 and i[w][h-1] == 'P':
                        temp = False
                        break
                    
                    if h+1 <= 4 and i[w][h+1] == 'P': 
                        temp = False
                        break
                    
                    if w-1 >= 0 and i[w-1][h] == 'P': 
                        temp = False
                        break
                    
                    if w+1 <= 4 and i[w+1][h] == 'P':
                        temp = False
                        break
                        
                        
                    # 대각으로 상좌 상우 하좌 하우
                    if (w-1 >= 0) and (h-1 >= 0) and (i[w-1][h-1] == 'P') and (i[w-1][h] != 'X' or i[w][h-1] != 'X'):
                        temp = False
                        break
                    
                    if (w-1 >= 0) and (h+1 <= 4) and (i[w-1][h+1] == 'P') and  (i[w-1][h] != 'X' or i[w][h+1] != 'X'):
                        temp = False
                        break
                    
                    if (w+1 <= 4) and (h-1 >= 0) and (i[w+1][h-1] == 'P') and (i[w+1][h] != 'X' or i[w][h-1] != 'X'):
                        temp = False
                        break
                    
                    if (w+1 <= 4) and (h+1 <= 4) and (i[w+1][h+1] == 'P') and (i[w+1][h] != 'X' or i[w][h+1] != 'X'):
                        temp = False
                        break
                        
                    # 상하좌우 두 칸씩
                    if h-2 >= 0 and i[w][h-2] == 'P' and i[w][h-1] != 'X':
                        temp = False
                        break
                    
                    if h+2 <= 4 and i[w][h+2] == 'P' and i[w][h+1] != 'X':
                        temp = False
                        break
                    
                    if w-2 >= 0 and i[w-2][h] == 'P' and i[w-1][h] != 'X':
                        temp = False
                        break
                    
                    if w+2 <= 4 and i[w+2][h] == 'P' and i[w+1][h] != 'X':
                        temp = False
                        break

            if not temp: break
        
        result.append(int(temp))
    
    return result