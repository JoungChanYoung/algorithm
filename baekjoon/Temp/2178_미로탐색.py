from collections import deque
m, n = map(int, input().split())

s = [[] for i in range(m)]
for i in range(m):
    tmp = input()
    for j in tmp:
        s[i].append(int(j))
# print(s)

visited = [[0 for i in range(n)] for j in range(m)]

q = deque()
x = y = 0 #current position
q.append((x,y)) #init
visited[y][x] = 1
result = 0

while(q):
    x, y = q.popleft()
    if x == n-1 and y == m-1:
        break
    tmp_result = visited[y][x]
    if y-1 >= 0 and not visited[y-1][x] and s[y-1][x]:
        q.append((x,y-1))
        visited[y-1][x] = tmp_result + 1
    if x-1 >= 0 and not visited[y][x-1] and s[y][x-1]:
        q.append((x-1,y))
        visited[y][x-1] = tmp_result + 1
    if y+1 <= m-1 and not visited[y+1][x] and s[y+1][x]:
        q.append((x,y+1))
        visited[y+1][x] = tmp_result + 1
    if x+1 <= n-1 and not visited[y][x+1] and s[y][x+1]:
        q.append((x+1,y))
        visited[y][x+1] = tmp_result + 1
    # print(q)
print(visited[m-1][n-1])
