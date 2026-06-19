def solution(arr, k):
    result = []
    seen = set()  
    
    for num in arr:
        if len(result) == k:
            break
        elif num not in seen:
            result.append(num)
            seen.add(num)

    while len(result) < k:
        result.append(-1)
        
    return result