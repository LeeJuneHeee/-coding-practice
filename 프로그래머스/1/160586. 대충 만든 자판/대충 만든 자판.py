def solution(keymap, targets):
    answer = []
    min_press = {}  

    for key in keymap:
        for i, char in enumerate(key):
            press_count = i + 1 
 
            if char in min_press:
                min_press[char] = min(min_press[char], press_count)
            else:
                min_press[char] = press_count
                
    # 2. targets의 각 문자열을 완성하기 위한 최소 클릭 수 계산
    for target in targets:
        total_press = 0
        is_possible = True
        
        for char in target:
            if char not in min_press:
                is_possible = False
                break
            total_press += min_press[char]
            
        if is_possible:
            answer.append(total_press)
        else:
            answer.append(-1)
            
    return answer