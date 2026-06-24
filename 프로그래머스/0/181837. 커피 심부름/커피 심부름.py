def solution(order):
    total_price = 0  
    
    for menu in order:
        
        if "cafelatte" in menu:
            total_price += 5000  
            
        else:
            total_price += 4500  
            
    return total_price