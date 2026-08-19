def count_divisors(num):
    count = 0
    for i in range(1, int(num ** 0.5) + 1):
        if num % i == 0:
            count += 1

            if i != num // i:
                count += 1
    return count

def solution(number, limit, power):
    total_iron = 0
    
    for n in range(1, number + 1):
        attack = count_divisors(n)
        
        if attack > limit:
            total_iron += power
        else:
            total_iron += attack
            
    return total_iron