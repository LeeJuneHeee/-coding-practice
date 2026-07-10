def solution(s):
    result = 0
    
    lists = s.split()
    
    count = 0
    
    for x in lists:
        if x != "Z":
            result += int(x)
            count += 1
        elif x == "Z":
            result -= int(lists[count - 1])
            count += 1
    
    return result