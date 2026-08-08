def solution(s, skip, index):
    alphabet = [c for c in "abcdefghijklmnopqrstuvwxyz" if c not in skip]
    
    result = ""
    
    for c in s:
        current_idx = alphabet.index(c)
        
        new_idx = (current_idx + index) % len(alphabet )
        
        result += alphabet[new_idx]
        
    return result