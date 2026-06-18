def solution(myString):
    answer = []
    
    part = myString.split('x')
    
    for c in part:
        if c != "":
            answer.append(c)
    
    answer.sort()
        
    return answer