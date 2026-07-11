def solution(sides):
    result = 0
    
    sorted_list = sorted(sides)
    
    if sorted_list[2] < sorted_list[0] + sorted_list[1]:
        return 1
    else:
        return 2