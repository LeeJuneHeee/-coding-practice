def solution(arr):
    stk = []
    
    for i in range(len(arr)):
        if len(stk) == 0:
            stk.append(arr[i])
        elif stk[-1] == arr[i]:
            stk.pop()
        else:
            stk.append(arr[i])
            
    if len(stk) == 0:
        return [-1]
        
    return stk