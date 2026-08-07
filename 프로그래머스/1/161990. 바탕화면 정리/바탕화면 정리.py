def solution(wallpaper):
    rows = []
    cols = []
    
    for r in range(len(wallpaper)):
        for c in range(len(wallpaper[0])):
            if wallpaper[r][c] == '#':
                rows.append(r)
                cols.append(c)
                
    lux = min(rows)
    luy = min(cols)
    rdx = max(rows) + 1  
    rdy = max(cols) + 1  
    
    return [lux, luy, rdx, rdy]