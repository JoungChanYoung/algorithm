from itertools import permutations
import math

def solution(numbers):
    answer = 0

    num_list = []
    for i in range(len(numbers)):
        num_list.append(numbers[i])

    tmp = []
    for k in range(len(num_list)):
        for i in permutations(num_list, k+1):
            tmp_num = int("".join(i))
            if tmp_num not in tmp:
                tmp.append(tmp_num)

    for i in range(len(tmp)):
        num = tmp[i]
        flag = 0
        if not num or num == 1:
            continue
        for j in range(2, math.floor(math.sqrt(num)) + 1):
            if num % j == 0:
                flag = 1
        if not flag:
            answer += 1
    return answer

if __name__ == "__main__":
    print (solution("011"))