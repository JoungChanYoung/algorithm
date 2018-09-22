#dp 5개까지는 초기값
# 이후에는 규칙 dp[x+1] = dp[x] + dp[x-4]
test_case = int(input())
dp = [0 for i in range(100)]
dp[0] = 1
dp[1] = 1
dp[2] = 1
dp[3] = 2
dp[4] = 2
for _ in range(test_case):
    num = int(input())
    for i in range(100):
        if i >= 5 :
            dp[i] = dp[i-1] + dp[i-5]
        if i == num-1:
            print(dp[i])
            break
