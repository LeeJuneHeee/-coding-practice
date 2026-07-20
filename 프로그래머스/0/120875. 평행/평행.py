def solution(dots):

    p1, p2, p3, p4 = dots
    
    def get_slope(dot1, dot2):
        return (dot2[1] - dot1[1]) / (dot2[0] - dot1[0])
        
    if get_slope(p1, p2) == get_slope(p3, p4):
        return 1
        
    if get_slope(p1, p3) == get_slope(p2, p4):
        return 1
        
    if get_slope(p1, p4) == get_slope(p2, p3):
        return 1
        
    return 0