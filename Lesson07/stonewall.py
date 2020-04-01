# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(heights):
    # write your code in Python 3.6
    stack = []
    counter = 0

    for h in heights:
        if stack:
            if stack[-1] == h:
                pass
            elif stack[-1] < h:
                stack.append(h)
                counter += 1
            else:
                while stack and stack[-1] > h:
                    stack.pop()
                if stack and stack[-1] == h:
                    pass
                else:
                    stack.append(h)
                    counter += 1
        else:
            stack.append(h)
            counter += 1
    return counter
