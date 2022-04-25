#level1 월간 코드 챌린지 시즌1
from itertools import combinations
def solution(numbers):
    answer = []
    for i in combinations(numbers, 2):
        tmp = sum(i)
        if tmp not in answer:
            answer.append(tmp)
    return sorted(answer)

if __name__ == "__main__":
    print(solution([2,1,3,4,1]))