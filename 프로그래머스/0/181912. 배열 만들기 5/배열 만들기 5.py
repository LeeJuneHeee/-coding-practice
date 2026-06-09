def solution(intStrs, k, s, l):
    answer = []
    
    for string in intStrs:
        sub_string = string[s : s + l]
        
        num = int(sub_string)
        
        if num > k:
            answer.append(num)
            
    return answer