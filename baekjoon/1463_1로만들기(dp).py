
# dp사용하기
# ex) 10은 3회 계산으로 만들수있음
# 10은 30,20에서도 쓰임 이걸 dp로 활용
import sys
n = int(input())
dp = [sys.maxsize for i in range(n+1)] # dp[k]는 k에서 1로만드는 연산 횟수의 최솟값

dp[1] = 0
for i in range(2,n+1):
    tmp1 = tmp2 = 0
    tmp3 = i - 1
    if i % 3 == 0:
        tmp1 = int(i / 3)
    if i % 2 == 0:
        tmp2 = int(i / 2)
    #print(dp[tmp1],dp[tmp2],dp[tmp3])
    opt = min([dp[tmp1], dp[tmp2], dp[tmp3]])
    dp[i] = opt + 1

print(dp[-1])
