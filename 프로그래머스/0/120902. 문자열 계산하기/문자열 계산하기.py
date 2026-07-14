def solution(my_string):
    
    tokens = my_string.split()
    
    result = int(tokens[0])
    
    for i in range(1, len(tokens), 2):
        operator = tokens[i]    
        next_num = int(tokens[i+1])
        
        if operator == "+":
            result += next_num
        elif operator == "-":
            result -= next_num
            
    return result