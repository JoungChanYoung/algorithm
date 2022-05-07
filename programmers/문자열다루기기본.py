#level1 연습문제

def solution(s):
    answer = True
    if not (len(s) == 4 or len(s) == 6):
        answer = False
    if not s.isdigit():
        answer = False
    return answer

if __name__ == "__main__":
    print(solution("1234"))