def solution(myString):
    result = []
    
    for c in myString:
        if c < 'l':
            result.append('l')
        else:
            result.append(c)
    
    return "".join(result)