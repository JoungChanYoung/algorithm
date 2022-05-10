#level1
import math
def solution(n):
    answer = 0

    if not math.sqrt(n) % 1:
        answer = math.floor(math.pow(math.sqrt(n)+1, 2))
    return answer or -1

if __name__ == "__main__":
    print(solution(121))