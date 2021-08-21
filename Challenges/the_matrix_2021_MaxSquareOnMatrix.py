# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")
def verify(A, K):
    i = 0
    while i < len(A):
        j = i
        while j < len(A) and A[j] >= K:
            j += 1
        # Range [i, j - 1] is ok
        if j - i >= K:
            return True
        i = max(j, i + 1)
    return False

def solution(A):
    # write your code in Python 3.6
    lower_bound, upper_bound = 1, len(A)
    while lower_bound < upper_bound:
        midpoint = (lower_bound + upper_bound + 1) // 2
        if verify(A, midpoint):
            lower_bound = midpoint
        else:
            upper_bound = midpoint - 1
    return lower_bound
