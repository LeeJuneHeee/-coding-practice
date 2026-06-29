def solution(babbling):
    answer = 0
    can_pronounce = ["aya", "ye", "woo", "ma"]
    
    for word in babbling:
        temp_word = word
        
        for speak in can_pronounce:
            temp_word = temp_word.replace(speak, " ")
            
        if temp_word.strip() == "":
            answer += 1
            
    return answer