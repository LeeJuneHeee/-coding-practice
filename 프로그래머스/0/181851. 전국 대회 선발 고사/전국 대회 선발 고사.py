def solution(rank, attendance):
    
    candidate = []
    
    for i in range(len(rank)):
        if attendance[i]:
            candidate.append([rank[i], i])
            
    candidate.sort()

    a = candidate[0][1]
    b = candidate[1][1]
    c = candidate[2][1]
    
    return a * 10000 + b * 100 + c