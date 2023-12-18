def solution(data):
    answer = {}
    for idx_x, x in enumerate(data):
        for idx_y, y in enumerate(x):
            if y == "#":
                try:
                    answer["x_min"] = idx_x if answer["x_min"] > idx_x else answer["x_min"]
                    answer["y_min"] = idx_y if answer["y_min"] > idx_y else answer["y_min"]
                    answer["x_max"] = idx_x if answer["x_max"] < idx_x else answer["x_max"]
                    answer["y_max"] = idx_y if answer["y_max"] < idx_y else answer["y_max"]
                except:
                    answer["x_min"] = idx_x
                    answer["y_min"] = idx_y
                    answer["x_max"] = idx_x
                    answer["y_max"] = idx_y
                    
    answer["x_max"] += 1
    answer["y_max"] += 1

    return list(answer.values())