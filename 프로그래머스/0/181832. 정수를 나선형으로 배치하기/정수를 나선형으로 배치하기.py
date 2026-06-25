def solution(n):
    answer = []
    for _ in range(n):
        row = []
        for _ in range(n):
            row.append(0)
        answer.append(row)

    dr = [0, 1, 0, -1]
    dc = [1, 0, -1, 0]
    
    r, c = 0, 0
    direction = 0 
    
    for num in range(1, n * n + 1):
        answer[r][c] = num 
        
        next_r = r + dr[direction]
        next_col = c + dc[direction]
        
        if next_r < 0 or next_r >= n or next_col < 0 or next_col >= n or answer[next_r][next_col] != 0:

            direction = (direction + 1) % 4
            
        r = r + dr[direction]
        c = c + dc[direction]
        
    return answer