# DP
# 계단 수 : 45656처럼 인접한 모든 자리의 수 차이가 1
# N길이의 수 중에 0~9까지 모든 수가 있는 계단 수의 개수 출력
# N: 10 -> 9876543210
# N: 11 -> 98765432101, 10123456789, 89876543210

#N은 하나만 주어진다.
#bit-masking 사용
N = int(input())
last = 10
bit = 1<<10

#dp[N][last][bit], N<=100 인 자연수, last는 마지막수(0~9), bit는 비트마스킹 1023인 수만 출력하면댐
dp = [[[0 for i in range(bit)] for i in range(last)] for i in range(N+1)]

for i in range(1,10):
    dp[1][i][1<<i] = 1

for i in range(2,N+1):
    for j in range(10):
        for k in range(bit):
            mask = k | (1<<j)
            tmp1 = 0
            tmp2 = 0
            if j>0 :
                tmp1 = dp[i-1][j-1][k]
            if j<9 :
                tmp2 = dp[i-1][j+1][k]
            dp[i][j][mask] = (dp[i][j][mask] + tmp1 + tmp2) % 1000000000

sum = 0
for i in range(10):
    sum = (sum + dp[N][i][1023]) % 1000000000

print(sum)
