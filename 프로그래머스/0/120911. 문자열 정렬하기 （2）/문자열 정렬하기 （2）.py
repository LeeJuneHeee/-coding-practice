def solution(my_string):
 
    my_string = my_string.lower()
    
    sorted_my_string = sorted(my_string)
    
    return "".join(sorted_my_string)
    
