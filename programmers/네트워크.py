#level3 dfs
from collections import deque
def solution(n, computers):
    answer = 0
    n = 0
    q = deque()
    
    visited = []
    for k in range(len(computers)):
        q.append(k)
        if k in visited:
            continue
        
        while q:
            i = q.popleft()
            visited.append(i)
            for j in range(len(computers[i])):
                if computers[i][j] and j not in visited:
                    q.append(j)
        answer += 1
    
    return answer

if __name__ == "__main__":
    print(solution(3,	[[1,0,0,0], [0, 1, 1, 0], [0, 1, 1, 1], [0, 0, 1, 1]]))