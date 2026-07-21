def solution(lines):

    blocks = [0] * 200
    
    for start, end in lines:

        for i in range(start + 100, end + 100):
            blocks[i] += 1
            
    duplicate_length = len([b for b in blocks if b >= 2])
    
    return duplicate_length