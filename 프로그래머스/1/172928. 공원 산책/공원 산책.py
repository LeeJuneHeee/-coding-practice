def solution(park, routes):
    H = len(park)
    W = len(park[0])
    
    for r in range(H):
        for c in range(W):
            if park[r][c] == 'S':
                y, x = r, c
                break
                
    direction = {
        'N': (-1, 0),
        'S': (1, 0),
        'W': (0, -1),
        'E': (0, 1)
    }
    
    for route in routes:
        op, n = route.split()  
        n = int(n)
        
        dy, dx = direction[op]
        
        ny, nx = y, x
        is_valid = True
        
        for _ in range(n):
            ny += dy
            nx += dx
            
            if not (0 <= ny < H and 0 <= nx < W):
                is_valid = False
                break
                
            if park[ny][nx] == 'X':
                is_valid = False
                break
                
        if is_valid:
            y, x = ny, nx
            
    return [y, x]