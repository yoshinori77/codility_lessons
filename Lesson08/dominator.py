# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")
from collections import defaultdict

def solution(A):
    # write your code in Python 3.6
    half_size = len(A)//2
    a_dict = defaultdict(list)

    for i, a in enumerate(A):
        a_dict[a].append(i)

    sort_a = sorted(a_dict.items(), key=(lambda x: len(x[1])))

    if half_size < len(sort_a[-1][1]):
        return sort_a[-1][1][0]
    else:
        return -1