import math

def solution(numer1, denom1, numer2, denom2):
    result_numer = (numer1 * denom2) + (numer2 * denom1)
    result_denom = denom1 * denom2
    
    gcd_value = math.gcd(result_numer, result_denom)
    
    answer = [result_numer // gcd_value, result_denom // gcd_value]
    
    return answer