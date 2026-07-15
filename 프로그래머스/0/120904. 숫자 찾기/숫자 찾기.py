def solution(num, k):
    
    num_str = str(num)
    k_str = str(k)
    
    idx = num_str.find(k_str)
    
    if idx == -1:
        return -1
    
    return idx + 1
    
