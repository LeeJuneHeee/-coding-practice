def solution(numbers, n):
    result = 0
    
    for i in range(len(numbers)):
        if result > n:
            return result
        else:
            result += numbers[i]
            
    return result
    
