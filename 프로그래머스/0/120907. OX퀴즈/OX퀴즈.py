def solution(quiz):
    result = []
    
    for q in quiz:
        tokens = q.split()
        
        x = int(tokens[0])
        operator = tokens[1]
        y = int(tokens[2])
        z = int(tokens[4])
        
        if operator == "+":
            real_result = x + y
        elif operator == "-":
            real_result = x - y
            
        if real_result == z:
            result.append("O")
        else:
            result.append("X")
    
    return result