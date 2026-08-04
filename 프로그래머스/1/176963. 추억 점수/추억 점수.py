def solution(name, yearning, photo):
    answer = []
    
    score_dict = dict(zip(name, yearning))
    
    for persons in photo:
        total_score = 0
        
        for person in persons:
            total_score += score_dict.get(person, 0)
            
        answer.append(total_score)
        
    return answer