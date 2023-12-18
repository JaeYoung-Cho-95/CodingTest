def solution(new_id):
    import re
    new_id = new_id.lower()
    
    new_id = re.findall(r'[0-9a-z-._]',new_id)
    new_id = ''.join(new_id)
    
    new_id = re.sub('\.{2,1000}','.',new_id)
    
    new_id = new_id.strip('.')
    
    if new_id == '':
        new_id = 'a'
        
    if len(new_id) >= 16:
        new_id = new_id[:15]
        new_id = new_id.strip('.')
    
    while True:
        if len(new_id) <= 2:
            new_id += new_id[len(new_id)-1]
            if len(new_id) >= 3:
                break
        else:
            break
    
    return new_id