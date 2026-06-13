def solution(str_list):
    answer = []
    
    for i, c in enumerate(str_list):
        if c == "l":
            for idx in range(i):
                answer.append(str_list[idx])
            return answer
        elif c == "r":
            return str_list[i + 1:]
    return []
            