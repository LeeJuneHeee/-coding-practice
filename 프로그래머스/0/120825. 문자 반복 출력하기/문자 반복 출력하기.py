def solution(my_string, n):
    result = ''
    
    for char in my_string:
        for i in range(n):
            result += char 
    
    return result