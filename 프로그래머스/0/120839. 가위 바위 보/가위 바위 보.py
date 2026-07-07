def solution(rsp):
    
    win_rules = {
        '2': '0',
        '0': '5',
        '5': '2'
    }
    
    result = ""
    
    for x in rsp:
        result += win_rules[x]
    
    return result