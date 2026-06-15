def solution(num_list):
    plus_result = 0
    multi_result = 1
    
    
    if len(num_list) >= 11:
        for num in range(len(num_list)):
            plus_result += num_list[num]
        return plus_result
    elif len(num_list) <= 10:
        for num in range(len(num_list)):
            multi_result *= num_list[num]
        return multi_result