#level3 dp
import sys
import math

answer = sys.maxsize

def dp(curr, N, number, cnt):
    global answer
    if cnt > 8:
        return
    elif number == curr:
        answer = min(answer, cnt)
        return
    tmp = ""
    for i in range(1, 9):
        tmp = str(tmp)
        tmp += str(N)
        tmp = int(tmp)
        dp(curr+tmp, N, number, cnt+i)
        dp(curr-tmp, N, number, cnt+i)        
        dp(curr//tmp, N, number, cnt+i)
        dp(curr*tmp, N, number, cnt+i)
    return
def solution(N, number):
    dp(0, N, number, 0)
    if answer == sys.maxsize:
        return -1
    return answer
    
if __name__ == "__main__":
    print(solution(5,26))

