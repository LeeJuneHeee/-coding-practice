def solution(str_list, ex):
    result = ''
    
    for i in range(len(str_list)):
        if ex not in str_list[i]:
            result += str_list[i]
    
    return result