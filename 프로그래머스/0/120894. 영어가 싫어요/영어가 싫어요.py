def solution(numbers):

    english_digits = [
        "zero", "one", "two", "three", "four", 
        "five", "six", "seven", "eight", "nine"
    ]
    
    for index, eng in enumerate(english_digits):
        numbers = numbers.replace(eng, str(index))
        
    return int(numbers)