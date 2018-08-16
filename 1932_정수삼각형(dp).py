n = int(input())
dp = []
for i in range(n):
    dp.append([0]*(i+1))

mat = []
dp[0][0] = int(input()) #첫 입력
for i in range(n-1):
    s = map(int,input().split())
    tmp = 0
    for j in s:
        if tmp > 0 and tmp < len(dp[i+1])-1 :
            dp[i+1][tmp] = max(dp[i][tmp-1]+j,dp[i][tmp]+j)
        elif tmp == 0 :
            dp[i+1][tmp] = dp[i][tmp] + j
        else :
            dp[i+1][tmp] = dp[i][tmp-1] + j
        tmp += 1
print(max(dp[-1]))
