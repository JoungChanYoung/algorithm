#level1 
from itertools import combinations
import math
def solution(nums):
    answer = 0

    tmp = [sum(i) for i in combinations(nums, 3)]
    
    for i in range(len(tmp)):
        flag = 0
        num = tmp[i]
        for j in range(math.floor(math.sqrt(num)) + 1):
            if j > 1 and num % j == 0:
                flag = 1
                break
        if not flag:
            answer += 1

    return answer

if __name__ == "__main__":
    print (solution([1,2,3,4]))