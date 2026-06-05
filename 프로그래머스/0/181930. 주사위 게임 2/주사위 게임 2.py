def solution(a, b, c):
    
    if a != b and b != c and c != a:
        return a + b + c
    elif a == b != c or b == c != a or a == c != b:
        return (a + b + c) * (a * a + b * b + c * c)
    elif a == b == c:
        return (a + b + c) * (a * a + b * b + c * c) * (a * a * a + b * b * b + c * c * c)
    