# 포도주 잔의 개수 n <= 10000
# 포도주 양은 1000이의 음이아닌 정수
# 세 잔 연달아 마실수 없음

#ex) 6, 10, 13, 9, 8, 10 이 있을때 33
n = int(input())
w = []
for i in range(n):
    w.append(int(input()))
dp = [[0 for j in range(3)] for i in range(n)] # dp[i] : i번째에 도착했을때 마실수 있는 최대 와인양

dp[0][1] = w[0]
for i in range(1,n):
    dp[i][0] = max(dp[i-1])
    dp[i][1] = max(dp[i-2]) + w[i]
    dp[i][2] = dp[i-1][1] + w[i]

print(max(dp[-1]))
