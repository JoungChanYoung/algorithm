#level1 연습문제
def solution(n):
    answer = [int(str(n)[i-1]) for i in range(len(str(n)), 0, -1)]
    return answer

if __name__ == "__main__":
    print(solution(17594))