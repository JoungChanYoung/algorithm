from collections import deque
n = int(input())

conn_num = int(input())

connection = [[] for i in range(n+1)]
visited = [0 for i in range(n+1)]
for i in range(conn_num):
    a, b = map(int, input().split())
    connection[a].append(b)
    connection[b].append(a)

q = deque()
q.append(1)
while(q):
    virus = q.popleft()
    if visited[virus]:
        continue
    for i in connection[virus]:
        q.append(i)
    visited[virus] = 1

result = -1
for i in visited:
    if i:
        result += 1
print(result)
