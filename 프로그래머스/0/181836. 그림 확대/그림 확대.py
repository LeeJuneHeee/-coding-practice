def solution(picture, k):
    answer = []  
    
    for row in picture:
        
        new_row = ""

        for char in row:
            new_row += char * k
            
        for _ in range(k):
            answer.append(new_row)
            
    return answer