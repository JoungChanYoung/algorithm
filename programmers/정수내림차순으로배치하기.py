#level1

def solution(n):
    answer = 0
    string_num = str(n)

    answer = "".join(sorted(string_num, reverse=True))
    return int(answer)

if __name__ == "__main__":
    print(solution(118372))