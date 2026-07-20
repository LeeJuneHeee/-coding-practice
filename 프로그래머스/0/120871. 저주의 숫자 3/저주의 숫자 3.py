def solution(n):
    town_num = 0 
    
    for _ in range(n):
        town_num += 1  

        while town_num % 3 == 0 or '3' in str(town_num):
            town_num += 1
            
    return town_num