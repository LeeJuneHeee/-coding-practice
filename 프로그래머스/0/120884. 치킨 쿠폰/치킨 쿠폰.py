def solution(chicken):
    result = 0 
    
    while chicken >= 10:
        service = chicken // 10
        leftover = chicken % 10
        
        result += service
        
        chicken = service + leftover

    return result