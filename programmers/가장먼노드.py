#level3 graph
from collections import deque
def solution(n, edge):
    answer = 0

    li = deque([[] for i in range(n + 1)])

    for i in range(len(edge)):
        li[edge[i][0]].append(edge[i][1])
        li[edge[i][1]].append(edge[i][0])

    distance = [0 for i in range(n+1)]
    visited = [0 for i in range(n+1)]
    q = deque()
    q.append((1, 0)) #1번 node 삽입

    #bfs로 최단 거리 정리
    dist = 0
    while q:
        tmp, dist = q.popleft()
        if not visited[tmp]:
            visited[tmp] = 1 #방문안한 노드 방문
            for i in range(len(li[tmp])):
                q.append((li[tmp][i], dist + 1)) #거리 값도 같이 저장
            distance[tmp] = dist + 1
    
    max_num = max(distance)
    for i in range(len(distance)):
        if distance[i] == max_num:
            answer += 1
    return answer

if __name__ == "__main__":
    print(solution(6, [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]))