def solution(array):
    
    max_value = max(array)
    
    max_idx = array.index(max_value)
    
    return [max_value, max_idx]