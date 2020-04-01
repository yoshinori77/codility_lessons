# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    # write your code in Python 3.6
    size = len(A)
    if size < 3:
        return 0
    sort_a = sorted(A)
    for i in range(size-2):
        p = sort_a[i]
        q = sort_a[i+1]
        r = sort_a[i+2]
        flg1 = p + q > r
        flg2 = q + r > p
        flg3 = r + p > q
        if flg1 and flg2 and flg3:
            return 1
    return 0
