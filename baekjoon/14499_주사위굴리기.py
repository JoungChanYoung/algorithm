N, M, x, y, k = map(int, input().split())

mat = [[0 for i in range(M)] for j in range(N)]
for i in range(N):
    tmp = input().split()
    for j in range(M):
        mat[i][j] = int(tmp[j])

#print(mat)
order = input().split()
for i in range(len(order)):
    order[i] = int(order[i])
#print(order)

cube = [[0 for i in range(3)] for j in range(4)]

def move(cube, mat, dir, r, c):
    if dir == 1: #east
        tmp = cube[3][1]
        cube[3][1] = cube[1][2]
        cube[1][2] = cube[1][1]
        cube[1][1] = cube[1][0]
        cube[1][0] = tmp
    if dir == 2: #west
        tmp = cube[1][2]
        cube[1][2] = cube[3][1]
        cube[3][1] = cube[1][0]
        cube[1][0] = cube[1][1]
        cube[1][1] = tmp
    if dir == 3: #north
        tmp = cube[3][1]
        cube[3][1] = cube[0][1]
        cube[0][1] = cube[1][1]
        cube[1][1] = cube[2][1]
        cube[2][1] = tmp
    if dir == 4: #south
        tmp = cube[2][1]
        cube[2][1] = cube[1][1]
        cube[1][1] = cube[0][1]
        cube[0][1] = cube[3][1]
        cube[3][1] = tmp
    if mat[r][c] is not 0:
        cube[3][1] = mat[r][c]
        mat[r][c] = 0
    elif mat[r][c] == 0:
        mat[r][c] = cube[3][1]

    return cube[1][1]

for i in order:
    tmpx,tmpy = x,y
    if i == 1 and y < M-1:
        y += 1
    elif i == 2 and y > 0:
        y -= 1
    elif i == 3 and x > 0:
        x -= 1
    elif i == 4 and x < N-1:
        x += 1
    if tmpx == x and tmpy == y:
        continue
    res = move(cube, mat, i, x, y)
    #print(cube)
    print(res)
