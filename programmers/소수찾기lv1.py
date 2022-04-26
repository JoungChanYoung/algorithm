#level1 연습문제
import math
def solution(n):
    answer = 0

    for i in range(2, n+1):
        flag = 1
        for j in range(2, math.floor(math.sqrt(i)) + 1):
            if i % j == 0:
                flag = 0
                break
        if flag:
            answer += 1
    return answer

if __name__=="__main__":
    print(solution(5))