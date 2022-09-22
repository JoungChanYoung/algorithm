N = int(input())

#init
dp = [[1 for j in range(10)] for i in range(N)]
dp[0][0] = 0

for i in range(1,len(dp)):
    for j in range(10):
        if j == 0:
            dp[i][j] = dp[i-1][j+1]
        elif j == 9:
            dp[i][j] = dp[i-1][j-1]
        else:
            dp[i][j] = (dp[i-1][j-1] + dp[i-1][j+1]) % 1000000000

print(sum(dp[-1]) % 1000000000)
