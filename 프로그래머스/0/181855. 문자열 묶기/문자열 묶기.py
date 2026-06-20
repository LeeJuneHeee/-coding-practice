def solution(strArr):
    len_counts = [0] * 32
    
    for word in strArr:
        word_len = len(word)
        
        len_counts[word_len] += 1
        
    return max(len_counts)