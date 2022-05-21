#level1
def solution(x, n):
    answer = []
    for i in range(n):
        answer += [x * (i+1)]
    return answer

if __name__ == "__main__":
    print(solution(2,	5))