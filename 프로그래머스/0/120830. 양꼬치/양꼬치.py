def solution(n, k):
    service_drink = n // 10
    
    return (n * 12000) + (k * 2000) - (service_drink * 2000)