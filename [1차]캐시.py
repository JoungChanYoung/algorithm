from collections import deque
def solution(cacheSize, cities):
    flag = 0
    answer = 0
    q = deque()
    for city in cities:
        c = city.lower()
        if c in q:
            answer += 1
            q.remove(c)
            q.append(c)
            continue
        else:
            answer += 5
            q.append(c)
        flag += 1
        if flag > cacheSize:
            q.popleft()
        print(q,answer)
    return answer

print(solution(3,['Jeju', 'Pangyo', 'Seoul', 'Jeju', 'Pangyo', 'Jeju', 'pohang', 'Pangyo', 'Seoul']))
