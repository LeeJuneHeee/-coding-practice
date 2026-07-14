def solution(s1, s2):
    result = 0
    
    for word in s1:
        if word in s2:
            result += 1
        
    return result