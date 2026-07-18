def solution(keyinput, board):
    
    x, y = 0, 0
    
    max_x = board[0] // 2
    max_y = board[1] // 2
    
    move = {
        "up" : (0, 1),
        "down" : (0, -1),
        "left" : (-1, 0),
        "right" : (1, 0)
    }
    
    for key in keyinput:
        dx, dy = move[key]
        
        next_x = x + dx
        next_y = y + dy
        
        if -max_x <= next_x <= max_x:
            x = next_x
        if -max_y <= next_y <= max_y:
            y = next_y
    
    return [x, y]