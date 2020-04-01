# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(S):
    # write your code in Python 3.6
    closing = {")": "("}
    stack = []

    for s in S:
        if s in closing:
            if not stack:
                return 0
            if stack[-1] != closing[s]:
                return 0
            else:
                stack.pop()
        else:
            stack.append(s)
    if stack:
        return 0
    else:
        return 1
