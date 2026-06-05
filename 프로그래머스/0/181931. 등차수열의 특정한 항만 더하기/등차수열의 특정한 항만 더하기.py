def solution(a, d, included):
    answer = 0
    current_value = a   
    
    for i in range(len(included)):
        if included[i] == True:
            answer += current_value
        
        current_value += d
    
    return answer