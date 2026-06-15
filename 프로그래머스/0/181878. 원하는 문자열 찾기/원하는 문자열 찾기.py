def solution(myString, pat):
    
    for i in range(len(myString)):
        if myString[i : i + len(pat)].lower() == pat.lower():
            return 1
        
        
    return 0
        
    
