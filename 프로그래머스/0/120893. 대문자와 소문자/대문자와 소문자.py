def solution(my_string):
    result = ''
    
    for char in my_string:
        if char.islower():
            result += char.upper()
        else:
            result += char.lower()
            
    return result