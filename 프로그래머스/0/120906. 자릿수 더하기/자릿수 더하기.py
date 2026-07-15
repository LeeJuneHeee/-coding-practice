def solution(n):
    
    result = 0
    
    str_n = str(n)
    
    for x in str_n:
        result += int(x)
    
    return result