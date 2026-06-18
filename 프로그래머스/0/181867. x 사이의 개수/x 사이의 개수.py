def solution(myString):
    split_list = myString.split('x')
    
    answer = []
    
    for c in split_list:
        c_length = len(c)
        
        answer.append(c_length)
    
    return answer