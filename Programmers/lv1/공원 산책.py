def checkover_or_findx(x, y, park, routes):
    route_length = int(routes[-1])
    park_x, park_y = len(park[0])-1, len(park)-1
    check = True
    if routes[0] == 'N':
        if y - route_length < 0:
            check = False
        else:
            for i in range(1,route_length+1):
                if park[y-i][x] == "X":
                    check = False
            if check:
                y = y-route_length
                    
    elif routes[0] == 'S':
        if y + route_length > park_y:
            check = False
        else:
            for i in range(1,route_length+1):
                if park[y+i][x] == "X":
                    check = False
        
            if check:
                y = y+route_length
            
    elif routes[0] == 'W':
        if x - route_length < 0:
            check = False
        else:
            for i in range(1,route_length+1):
                if park[y][x-i] == "X":
                    check = False
            if check:
                x = x - route_length
                
    elif routes[0] == 'E':
        if x + route_length > park_x:
            check = False
        else:
            for i in range(1,route_length+1):
                if park[y][x+i] == "X":
                    check = False
            if check:
                x = x + route_length
    
    return int(x), int(y)

def solution(park, routes):
    start_x, start_y = 0, 0
    for idx_y, y in enumerate(park):
        for idx_x, x in enumerate(y):
            if park[idx_y][idx_x] == "S":
                start_x, start_y = idx_x, idx_y
    
    for route in routes:
        start_x, start_y = checkover_or_findx(start_x, start_y, park, route)
    
    return [start_y,start_x]
    