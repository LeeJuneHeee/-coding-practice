def solution(array, n):
    array.sort()
    
    closest_num  = array[0]
    min_distance = abs(array[0] - n)
    
    for num in array:
        current = abs(num - n)
        
        if current < min_distance:
            min_distance = current
            closest_num = num
    
    return closest_num