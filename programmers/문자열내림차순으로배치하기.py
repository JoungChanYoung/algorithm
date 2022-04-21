#level1 연습문제

def solution(s):
    answer = ''
    answer = "".join(sorted(s,reverse=True))
    return answer

if __name__ == "__main__":
    print(solution("Zbcdefg"))