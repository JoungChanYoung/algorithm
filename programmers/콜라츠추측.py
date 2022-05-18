#level1 

def solution(num):
    answer = -1
    if num == 1:
        return 0
    for i in range(500):
        if num % 2 == 0:
            num /= 2
        else:
            num *= 3
            num += 1
        if num == 1:
            answer = i+1
            break
    return answer

if __name__ == "__main__":
    print(solution(1))