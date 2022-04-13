#level2 2017 팁스타운
from collections import deque
def solution(s):
    answer = -1
    
    stack = deque()
    stack.append(s[0])

    for i in range(1, len(s)):
        if stack and s[i] == stack[-1]:
            stack.pop()
        else:
            stack.append(s[i])
    if not stack:
        return 1
    else:
        return 0

if __name__ == "__main__":
    print(solution("baabaa"))
    #abcdeedcba