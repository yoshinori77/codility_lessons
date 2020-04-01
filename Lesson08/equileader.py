# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")
from collections import defaultdict


def solution(A):
    # write your code in Python 3.6
    count = 0
    a_dict = defaultdict(int)
    num = 0
    max_count = 0

    for a in A:
        a_dict[a] += 1
        if max_count < a_dict[a]:
            max_count = a_dict[a]
            num = a

    left = 0
    right = max_count
    result = 0

    for i, a in enumerate(A, 1):
        if a == num:
            left += 1
            right -= 1
        if i // 2 < left and (len(A) - i) // 2 < right:
            result += 1
    return result
