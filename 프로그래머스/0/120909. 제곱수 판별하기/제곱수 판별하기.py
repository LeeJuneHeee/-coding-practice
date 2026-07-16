def solution(n):
    
    value = n ** 0.5
    
    if value % 1 == 0:
        return 1
    else:
        return 2