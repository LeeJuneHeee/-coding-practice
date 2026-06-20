def solution(arr1, arr2):
    
    arr1_value = 0
    arr2_value = 0
    
    if len(arr1) > len(arr2):
        return 1 
    elif len(arr1) < len(arr2):
        return -1
    else:
        for num1 in arr1:
            arr1_value += num1
        for num2 in arr2:
            arr2_value += num2
        if arr1_value > arr2_value:
            return 1
        elif arr2_value > arr1_value:
            return -1
        else:
            return 0