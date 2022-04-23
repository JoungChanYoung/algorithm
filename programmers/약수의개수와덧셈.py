#level1 월간코드챌린지2
import math
def solution(left, right):
    answer = 0
    for i in range(left, right + 1):
        if i % math.sqrt(i) == 0:
            answer -= i
        else:
            answer += i
    return answer

if __name__ == "__main__":
    print(solution(13, 17))