def solution(num_list):
    multiplication = 1
    square = 0
    
    for i in num_list:
        multiplication *= i
        
    for i in num_list:
        square += i
    
    square = square * square
    
    if multiplication < square:
        return 1
    else:
        return 0