def solution(age):
    answer = ""
    for digit in str(age):
        answer += chr(int(digit) + 97)
    return answer