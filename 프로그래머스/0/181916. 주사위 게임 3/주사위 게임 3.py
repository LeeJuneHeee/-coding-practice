def solution(a, b, c, d):
    
    dice = sorted([a, b, c, d])
    
    if dice[0] == dice[1] == dice[2] == dice[3]:
        return 1111 * dice[0]
    elif dice[0] == dice[1] == dice[2]:  # 앞의 3개가 같을 때
        p = dice[0]
        q = dice[3]
        return (10 * p + q) ** 2
    elif dice[1] == dice[2] == dice[3]:  # 뒤의 3개가 같을 때
        p = dice[1]
        q = dice[0]
        return (10 * p + q) ** 2
    elif dice[0] == dice[1] and dice[2] == dice[3]: # 정렬되었기 때문에 앞의 2개 뒤의 2개
        p = dice[0]
        q = dice[2]
        return (p + q) * abs(p - q)
    elif dice[0] == dice[1]:  # 앞의 2개가 같을 때 
        return dice[2] * dice[3]
    elif dice[1] == dice[2]:  # 가운데 2개가 같을 때 
        return dice[0] * dice[3]
    elif dice[2] == dice[3]:  # 뒤의 2개가 같을 때
        return dice[0] * dice[1]
    else: # 네개 모두 다른 경우
        return dice[0]
        
        
        
        