def solution(my_string):

    for char in my_string:
        if char.isalpha(): 
            my_string = my_string.replace(char, " ")
            
    numbers = my_string.split()
    
    return sum([int(num) for num in numbers])