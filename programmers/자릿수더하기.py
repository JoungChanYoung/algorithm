#level1 연습문제

def solution(n):
    answer = 0
    string = str(n)
    answer = sum([int(i) for i in string])
    return answer

if __name__ == "__main__":
    print(solution(123))