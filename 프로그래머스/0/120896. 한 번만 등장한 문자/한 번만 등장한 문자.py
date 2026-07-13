def solution(s):
    answer = []

    for char in s:
        if s.count(char) == 1:
            answer.append(char)
            
    sorted_list = sorted(answer)
    
    return "".join(sorted_list)