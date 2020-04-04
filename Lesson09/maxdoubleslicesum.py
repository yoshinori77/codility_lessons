# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

# https://codesays.com/2014/solution-to-max-double-slice-sum-by-codility/#comment-870

# ポイント1. 左から右、右から左方向に累積和を計算した配列を作る。
# ポイント2. 上記の2つの配列を組み合わせる。一つ飛ばしにするため（Y)、最初の配列はi, 二つ目の配列はi+2の要素を足す

def solution(A):
    # write your code in Python 3.6
    n = len(A)
    left = [0] * n
    for i in range(1, n-1):
        left[i] = max(0, left[i-1] + A[i])

    right = [0] * n
    for i in range(n-2, 1, -1):
        right[i] = max(0, right[i+1] + A[i])

    max_sum = 0
    for i in range(1, n-1):
        max_sum = max(max_sum, left[i-1] + right[i+1])
    return max_sum
