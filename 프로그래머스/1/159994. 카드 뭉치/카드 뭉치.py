def solution(cards1, cards2, goal):
    idx1 = 0
    idx2 = 0
    
    for c in goal:
        if idx1 < len(cards1) and cards1[idx1] == c:
            idx1 += 1
        elif idx2 < len(cards2) and cards2[idx2] == c:
            idx2 += 1
        else:
            return "No"
        
    return "Yes"