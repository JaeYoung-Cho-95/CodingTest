def solution(numbers, hand):
    answer = ''
    num_col = '1 2 3 4 5 6 7 8 9 * 0 #'.split()
    temp = dict()
    x,y = 0,0
    for i in num_col:
        temp[i] = (x,y)
        x += 1
        if x == 3:
            x = 0
            y += 1

    left = (0,3)
    right = (2,3)

    for i in numbers:
        target_x, target_y = temp['{}'.format(i)]
        
        if target_x == 0:
            left = (target_x, target_y)
            answer += 'L'
        elif target_x == 2:
            right = (target_x, target_y)
            answer += 'R'
        elif target_x == 1:
            l_x, l_y = left
            r_x, r_y = right

            l_distance = abs((l_x - target_x)) + abs((l_y - target_y))
            r_distance = abs((r_x - target_x)) + abs((r_y - target_y))

            if l_distance > r_distance:
                right = (target_x,target_y)
                answer += 'R'
            elif l_distance < r_distance:
                left = (target_x,target_y)
                answer += 'L'
            else:
                if hand =='right':
                    right = (target_x,target_y)
                    answer += 'R'
                else:
                    left = (target_x,target_y)
                    answer += 'L'
    return answer