def solution(arr):
    two_square = [1, 2, 4, 8 , 16, 32, 64, 128, 256, 512, 1024]
    
    current_len = len(arr)
    
    target_len = 0
    for num in two_square:
        if num >= current_len:
            target_len = num
            break
    
    count = target_len - current_len
    
    arr += [0] * count
    
    return arr