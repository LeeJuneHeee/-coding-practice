def solution(my_string, overwrite_string, s):
    front = my_string[:s]
    
    middle = overwrite_string
    
    end = my_string[s + len(overwrite_string):]
    
    answer = front + middle + end
    
    return answer