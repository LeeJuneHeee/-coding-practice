def solution(players, callings):
    player_list = {}
    for i, player in enumerate(players):
        player_list[player] = i
    
    for calling in callings:
        current_idx = player_list[calling]
        front_idx = current_idx - 1 
        
        front_player = players[front_idx]
        
        players[front_idx] = calling
        players[current_idx] = front_player
        
        player_list[calling] = front_idx
        player_list[front_player] = current_idx
        
    return players