def solution(a, b):
    ab = int(str(a) + str(b))
    ab_p = 2 * a * b
    
    if ab > ab_p:
        return ab
    elif ab == ab_p:
        return ab
    else: 
        return ab_p