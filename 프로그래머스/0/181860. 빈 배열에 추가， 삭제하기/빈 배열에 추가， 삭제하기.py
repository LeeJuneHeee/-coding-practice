def solution(arr, flag):
    X = []
    
    for i, num in enumerate(arr):
        if flag[i]:
            X += [num] * (num * 2)
        else:
            for _ in range(num):
                X.pop()
        
    return X