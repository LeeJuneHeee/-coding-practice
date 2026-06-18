def solution(myString, pat):
    new_myString = ""
    
    for c in myString:
        if c == "A":
            new_myString += "B"
        elif c == "B":
            new_myString += "A"
    
    if pat in new_myString:
        return 1
    else:
        return 0