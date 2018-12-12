#save data
row, col = map(int,input().split())

mat = [[0 for j in range(col)] for i in range(row)]
for y in range(row):
    tmp = map(int,input().split())
    x = 0
    for t in tmp:
        mat[y][x] = t
        x += 1

dp = [[-1 for j in range(col)] for i in range(row)]

direction_x = [0, 1, 0, -1]
direction_y = [1, 0, -1, 0]

def func(x, y):
    if y == row-1 and x == col-1 :
        return 1
    if dp[y][x] is not -1:
        return dp[y][x]
    dp[y][x] = 0
    for i in range(4):
        nx = x + direction_x[i]
        ny = y + direction_y[i]
        if nx < 0 or nx >= col or ny < 0 or ny >= row:
            continue
        elif mat[y][x] > mat[ny][nx]:
            dp[y][x] += func(nx, ny)
    return dp[y][x]

print(func(0,0))
print(dp)
