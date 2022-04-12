#level1 월간 코드 챌린지 시즌1
def solution(a, b):
    answer = 0
    for i, j in zip(a, b):
        answer += i*j
    return answer

if __name__ == "__main__":
    solution([-1,0,1],[1,0,-1])