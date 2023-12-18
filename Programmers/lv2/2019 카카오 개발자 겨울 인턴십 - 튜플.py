def solution(s):
    s = s.replace('{','[').replace('}',']')
    jiwon = eval(s)

    jiwon.sort(key=lambda x : len(x))

    result = [jiwon[0][0]]
    
    for i in range(1,len(jiwon)):
        
        for j in jiwon[i]:
            
            if j not in jiwon[i-1]:
                result.append(j)

                
    return result