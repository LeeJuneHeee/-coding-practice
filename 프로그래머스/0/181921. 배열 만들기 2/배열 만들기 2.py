def solution(l, r):
    answer = []
    
    for num in range(l, r + 1):
        num_set = set(str(num))
        
        if num_set.issubset({'5', '0'}):
            answer.append(num)
        
    if answer:
        return answer
    else:
        return [-1]