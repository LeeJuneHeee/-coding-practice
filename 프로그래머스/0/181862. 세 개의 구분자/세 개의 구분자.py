import re

def solution(myStr):
    answer = []
    
    parts = re.split('[abc]', myStr)
    
    for string in parts:
        if string != "":
            answer.append(string)
            
    if len(answer) == 0:
        return ["EMPTY"]
        
    return answer