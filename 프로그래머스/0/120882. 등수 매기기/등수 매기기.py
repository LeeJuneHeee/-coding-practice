def solution(score):

    total_scores = [sum(s) for s in score]

    sorted_scores = sorted(total_scores, reverse=True)
    
    return [sorted_scores.index(total) + 1 for total in total_scores]