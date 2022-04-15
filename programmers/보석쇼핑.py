#level3 2020 카카오 인턴십
from collections import Counter
import sys
def solution(gems):
    answer = []
    count_gems = len(Counter(gems))
    tmp = Counter(gems)

    #two point algorithm
    end = 0
    len_gems = len(gems)
    min_num = sys.maxsize
    min_range = []
    sub_gems = {}
    for start in range(len_gems):
        while len(sub_gems) < count_gems and end < len_gems:
            if gems[end] not in sub_gems.keys():
                sub_gems[gems[end]] = 1
            else:
                sub_gems[gems[end]] += 1
            end += 1
        if count_gems == len(sub_gems) and min_num > end-start:
            min_num = end-start
            min_range = [start+1, end]

        sub_gems[gems[start]] -= 1
        if sub_gems[gems[start]] == 0:
            del sub_gems[gems[start]]
    answer = min_range
    return answer

if __name__ == "__main__":
    print(solution(["AA", "AB", "AC", "AA", "AC"]))