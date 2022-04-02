#level2 greedy
from collections import deque

def solution(people, limit):
    answer = 0

    people = deque(sorted(people))
    limit_tmp = limit
    while people:
        if limit_tmp == limit:
            max_person = people.pop()
            limit_tmp -= max_person
            if not people:
                answer += 1
        else:
            min_person = people.popleft()
            limit_tmp -= min_person
            if limit_tmp < 0:
                people.appendleft(min_person)
                answer += 1
                limit_tmp = limit
            elif limit_tmp == 0:
                answer += 1      
                limit_tmp = limit
            elif not people:
                answer += 1
    return answer

if __name__ == "__main__":
    print(solution ([100], 100))