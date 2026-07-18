def solution(numbers):
    
    numbers.sort()
    
    a = numbers[0] * numbers[1]
    b = numbers[-1] * numbers[-2]
    
    
    if a > b:
        return a
    elif a < b:
        return b
    else:
        return a
