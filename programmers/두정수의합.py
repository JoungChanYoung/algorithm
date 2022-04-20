def solution(a, b):
    answer = 0
    if b < a:
        tmp = b
        b = a
        a = tmp
    for i in range(a, b + 1):
        answer += i
    return answer

if __name__ == "__main__":
    print(solution(3, 5))