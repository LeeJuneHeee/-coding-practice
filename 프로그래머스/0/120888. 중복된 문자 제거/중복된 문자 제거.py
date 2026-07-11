def solution(my_string):
    result = ''

    for x in my_string:
        if x not in result:
            result += x
    
    return result