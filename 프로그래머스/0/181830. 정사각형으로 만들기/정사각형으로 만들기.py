def solution(arr):

    row_count = len(arr)
    col_count = len(arr[0])
    

    if row_count > col_count:
        diff = row_count - col_count
        
        for row in arr:
            for _ in range(diff):
                row.append(0)
                
    elif col_count > row_count:
        diff = col_count - row_count
        
        for _ in range(diff):
            new_row = []
            for _ in range(col_count):
                new_row.append(0)
            arr.append(new_row)
            
    return arr