def solution(emergency):
    
    sorted_emergency = sorted(emergency, reverse = True)
    
    result = []
    
    for i in emergency:
        rank = sorted_emergency.index(i) + 1
        result.append(rank)
    
    return result