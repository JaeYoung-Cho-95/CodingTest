def solution(babbling):
    can_pronounce = ["aya", "ye", "woo", "ma"]
    
    cnt = 0
    for word in babbling:
        while True:
            if len(word) == 0:
                cnt += 1
                break
            if word[:2] in can_pronounce:
                word = word.replace(f"{word[:2]}", "")
            elif word[:3] in can_pronounce:
                word = word.replace(f"{word[:3]}", "")
            else:
                break
    return cnt


if __name__ == "__main__":
    x = "asd"
    x = x.replace("a", "")
    print(x)
