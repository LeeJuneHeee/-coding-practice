def solution(arr, queries):
    
    result = []
    
    for s, e, k in queries:
        candidates = []
        
        for i in range(s, e + 1):
            if arr[i] > k:
                candidates.append(arr[i])
        
        if candidates:
            result.append(min(candidates))
        else:
            result.append(-1)
    
    return result
        