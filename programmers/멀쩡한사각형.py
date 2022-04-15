#level2 summer/winter coding 2019
from math import gcd
def solution(w,h):
    answer = w*h - (w+h - gcd(w,h))
    return answer

if __name__ == "__main__":
    print(solution(8, 12))