def solution(numbers, k):
    
    target_index = (k - 1) * 2
    
    final_index = target_index % len(numbers)
    
    return numbers[final_index]