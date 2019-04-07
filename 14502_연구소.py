
from collections import deque
import copy

row, col = map(int,input().split())

mat = [[0 for j in range(col)] for i in range(row)]
for i in range(row):
    a = input().split()
    for j in range(len(a)):
        mat[i][j] = int(a[j])
q = deque()
def bfs(mat_tmp, idx_2):
    for a,b in idx_2:
        q.append((a,b))
    num = 0
    visit = [[0 for j in range(col)] for i in range(row)]
    while(q): #바이러스 확산 끝날때까지 수행
        r, c = q.popleft()
        if visit[r][c]:
            continue
        if r-1 >= 0 and visit[r-1][c] == 0 and mat_tmp[r-1][c] == 0: #빈칸이면 확산
            mat_tmp[r-1][c] = 2
            q.append((r-1, c))
        if r+1 < row and visit[r+1][c] == 0 and mat_tmp[r+1][c] == 0:
            mat_tmp[r+1][c] = 2
            q.append((r+1, c))
        if c-1 >= 0 and visit[r][c-1] == 0 and mat_tmp[r][c-1] == 0:
            mat_tmp[r][c-1] = 2
            q.append((r, c-1))
        if c+1 < col and visit[r][c+1] == 0 and mat_tmp[r][c+1] == 0:
            mat_tmp[r][c+1] = 2
            q.append((r, c+1))
        visit[r][c] = 1
        #print(q)

    for i in range(row):
        for j in range(col):
            if mat_tmp[i][j] == 0:
                num += 1
    return num

result = 0
idx = []
idx_2 = []
for i in range(row): #벽3개 세우는 모든 경우의 수
    for j in range(col):
        if mat[i][j] == 0: #0
            idx.append((i,j)) #0 있는 idx 모두 저장
        elif mat[i][j] == 2:
            idx_2.append((i,j))

for a in range(len(idx)-2):
    for b in range(a+1,len(idx)-1):
        for c in range(b+1,len(idx)):
            mat_tmp = copy.deepcopy(mat)
            i1, j1 = idx[a]
            i2, j2 = idx[b]
            i3, j3 = idx[c]
            mat_tmp[i1][j1] = mat_tmp[i2][j2] = mat_tmp[i3][j3] = 1

            tmp = bfs(mat_tmp, idx_2)
            if result < tmp:
                result = tmp

print(result)
