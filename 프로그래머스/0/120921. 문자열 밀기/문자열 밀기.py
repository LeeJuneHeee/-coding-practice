def solution(A, B):

    if A == B:
        return 0

    for count in range(1, len(A) + 1):
        A = A[-1] + A[:-1]

        if A == B:
            return count
            
    return -1