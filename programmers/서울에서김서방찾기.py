#level1 연습문제

def solution(seoul): 
    answer = seoul.index("Kim")
    return "김서방은 " + str(answer) + "에 있다"

if __name__ == "__main__":
    print(solution(["Jane", "Kim"]))