#level1 월간 코드 챌린지 시즌3

def solution(n):
    for i in range(2, n):
        if n % i == 1:
            return i

if __name__ == "__main__":
    print(solution(5))