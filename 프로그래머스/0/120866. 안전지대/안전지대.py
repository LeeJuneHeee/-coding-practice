def solution(board):
    n = len(board) 

    danger_board = [[0] * n for _ in range(n)]
    
    adjacent = [
        (-1, -1), (-1, 0), (-1, 1),
        (0, -1),  (0, 0),  (0, 1),
        (1, -1),  (1, 0),  (1, 1)
    ]

    for r in range(n):
        for c in range(n):
            if board[r][c] == 1:
                for dr, dc in adjacent:
                    nr = r + dr
                    nc = c + dc
                    
                    if 0 <= nr < n and 0 <= nc < n:
                        danger_board[nr][nc] = 1 
                        
    safe_count = 0
    for r in range(n):
        for c in range(n):
            if danger_board[r][c] == 0:
                safe_count += 1
                
    return safe_count