#level1 
import math
def solution(n, m):
    answer = [math.gcd(n,m), math.floor(n*m/ math.gcd(n,m))]
    return answer

if __name__ == "__main__":
    print(solution(3, 12))