def solution(arr):
    if 2 not in arr:
        return [-1]
    
    start_idx = arr.index(2)
    
    end_idx = len(arr) - 1 - arr[::-1].index(2)
    
    return arr[start_idx:end_idx + 1]