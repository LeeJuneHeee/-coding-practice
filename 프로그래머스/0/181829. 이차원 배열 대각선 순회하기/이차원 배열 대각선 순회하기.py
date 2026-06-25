def solution(board, k):
    total_sum = 0 

    row_count = len(board)
    col_count = len(board[0])
    
    for i in range(row_count):
        for j in range(col_count):
            if i + j <= k:
                total_sum += board[i][j]
                
    return total_sum