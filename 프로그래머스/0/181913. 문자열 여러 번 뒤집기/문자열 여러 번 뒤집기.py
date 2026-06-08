def solution(my_string, queries):
    arr = list(my_string)
    
    for i, j in queries:
        arr[i:j+1] = arr[i:j+1][::-1]
        
    return "".join(arr)