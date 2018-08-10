import sys
n = int(input())#n<=1000

s = [[0]*3 for i in range(n+1)]
for x in range(n):
    r,g,b = map(int,input().split())
    s[x][0] = r
    s[x][1] = g
    s[x][2] = b
cost = [[sys.maxsize]*3 for i in range(n)]

cost[0][0] = s[0][0]
cost[0][1] = s[0][1]
cost[0][2] = s[0][2]
for y in range(len(s)-2):
    cost[y+1][0] = min([cost[y][1],cost[y][2]]) + s[y+1][0]
    cost[y+1][1] = min([cost[y][0],cost[y][2]]) + s[y+1][1]
    cost[y+1][2] = min([cost[y][0],cost[y][1]]) + s[y+1][2]
print(min(cost[-1]))
