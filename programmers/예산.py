#level1
from itertools import combinations
def solution(d, budget):
    answer = 0
    s = sorted(d)

    flag = 0 
    for i in range(len(s)):
        budget -= s[i]       
        if budget < 0:
            flag = 1
            answer = i
            break
        elif budget == 0:
            flag = 1
            answer = i + 1
            break

    if flag:
        return answer
    else:
        return len(d)
if __name__ == "__main__":
    print(solution([1, 3, 2, 5, 4], 9))