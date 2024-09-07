from collections import deque

x = input()

result = deque()
temp = deque()

idx = 0
while True:
    if x[idx] == "<":
        temp = "".join(list(temp)[-1::-1])
        result.append(temp)
        temp = deque()
        temp.append(x[idx])
        while True:
            idx += 1
            temp.append(x[idx])
            if x[idx] == ">":
                temp = "".join(list(temp))
                result.append(temp)
                temp = deque()
                break
                
    elif x[idx] == " ":
        temp = "".join(list(temp)[-1::-1])
        result.append(temp)
        temp = deque()
        result.append(" ")
        
    else:
        temp.append(x[idx])
    
    idx += 1
    if idx >= len(x):
        temp = "".join(list(temp)[-1::-1])
        result.append(temp)
        break
    
    
[print(x, end="") for x in result]