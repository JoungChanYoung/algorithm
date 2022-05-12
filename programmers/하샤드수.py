#level1 연습문제
def solution(x):
    answer = True
    s = str(x)
    result = 0
    for i in s:
        result += int(i)
    if x % result != 0:
        answer = False
    
    return answer

if __name__ == "__main__":
    solution(10)