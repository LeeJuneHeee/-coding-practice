def solution(my_string):
    answer = 0
    
    num = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
    
    for x in my_string:
        if x in num:
            answer += int(x)
            
    return answer