def solution(s):
    formula = {'S':1,'D':2,'T':3,'*':2,'#':-1}
    nums, multi, anchor = [],[],[]
    cnt = 0
    for i in range(len(s)):
        if ord(s[i]) > 58:
            nums.append(s[cnt:i])
            multi.append(s[i])
            try:
                if ord(s[i+1]) <= 47:
                    anchor.append(s[i+1])
                    cnt = i + 2
                else:
                    anchor.append(' ')
                    cnt = i + 1
            except: anchor.append(' ')

    for i in range(3):
        nums[i] = int(nums[i]) ** formula[multi[i]]
        try:
            if anchor[i] == '*':
                nums[i] = int(nums[i]) * formula[anchor[i]]
                if i >= 1:    
                    nums[i-1] = int(nums[i-1]) * formula[anchor[i]]
            elif anchor[i] == '#':
                nums[i] = int(nums[i]) * formula[anchor[i]]    
        except:pass
    return sum(nums)