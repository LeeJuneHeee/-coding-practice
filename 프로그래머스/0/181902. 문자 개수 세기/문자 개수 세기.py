def solution(my_string):
    result = [0] * 52
    
    for c in my_string:
        if c.isupper():
            i = ord(c) - ord('A')
            result [i] += 1
        elif c.islower():
            i = ord(c) - ord('a') + 26
            result[i] += 1
    
    return result