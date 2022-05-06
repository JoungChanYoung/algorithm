#level1 위클리챌린지

def solution(price, money, count):
    answer = -1

    answer = sum([price*(count-i) for i in range(count)])
    if money > answer:
        return 0
    return answer-money

if __name__ == "__main__":
    print(solution(3, 20, 4))