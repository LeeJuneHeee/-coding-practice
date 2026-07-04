def solution(num_list):
    odd_count = 0
    even_count = 0

    answer = []
    
    for i in range(len(num_list)):
        if num_list[i] % 2 == 1:
            odd_count += 1
        else:
            even_count += 1

    answer.append(even_count)
    answer.append(odd_count)

    return answer