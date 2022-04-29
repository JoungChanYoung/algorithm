#level1 연습문제
import math
def solution(n):
    answer = 0
    for i in range(1, math.floor(math.sqrt(n))+1):
        if i == math.sqrt(n):
            answer += i
        elif n % i == 0:
            answer = answer + i + math.floor(n/i)
    return answer

if __name__ == "__main__":
    print(solution(12))