def solution(num, total):
    center = total // num
    
    start = center - ((num - 1) // 2)
    
    return [start + i for i in range(num)]