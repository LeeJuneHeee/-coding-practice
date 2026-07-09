def solution(box, n):
    width = box[0] // n
    length = box[1] // n
    heigth = box[2] // n
    
    return width * length * heigth