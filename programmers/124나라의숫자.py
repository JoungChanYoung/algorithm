#level2
from collections import deque
def solution(n):
    answer = ''
    q = deque()
    if n <= 2:
        return str(n)
    elif n == 3:
        return '4'

    while n >= 3:
        remainder = n % 3
        quotient = n // 3                   

        if remainder == 0:
            remainder = 4
            quotient -= 1          

        q.appendleft(str(remainder))
        if quotient and quotient < 3:
            q.appendleft(str(quotient))
        n = quotient
    
    answer = "".join(q)
    return answer

if __name__=="__main__":
    print(solution(10))