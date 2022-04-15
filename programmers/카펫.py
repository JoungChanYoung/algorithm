#level2 완전탐색
import math
def solution(brown, yellow):
    answer = [0 for i in range(2)]
    tmp = brown + yellow
    m = n = 3
    for m in range(3, math.floor(tmp/3) + 1):
        if tmp % m == 0: #m, n은 brown + yellow의 약수만 가능
            n = int(tmp / m)
            if 2 * m + 2 * n - 4  == brown and m >= n:
                answer[0], answer[1] = m, n
                break
    return answer

if __name__ == "__main__":
    print(solution(24,24))