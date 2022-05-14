#level1

def solution(num):
    answer = 'Even'
    if num % 2 == 1:
        answer = 'Odd'
    return answer

if __name__ == "__main__":
    solution(3)