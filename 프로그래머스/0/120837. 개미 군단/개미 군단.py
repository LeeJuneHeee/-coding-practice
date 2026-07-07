def solution(hp):
    answer = 0
    
    general = hp // 5
    first_last_hp = hp % 5
    
    soldier = first_last_hp // 3
    second_last_hp = first_last_hp % 3
    
    worker = second_last_hp // 1
    final_last_hp = second_last_hp % 1
    
    return general + soldier + worker