#level3 dp
def solution(m, n, puddles):
    answer = 0
    dp = [[0 for j in range(m+1)] for i in range(n+1)]
    
    for i in range(len(puddles)):
        a, b = puddles[i]
        dp[b][a] = -1
    
    dp[0][1] = 1
    dp[1][0] = 0
    for i in range(1, n+1):
        for j in range(1, m+1):
            if dp[i][j] == -1:
                continue
            elif dp[i][j-1] == -1:#왼쪽이 물웅덩이인 경우
                if dp[i-1][j] != -1: #위쪽을 먼저 가져오고
                    dp[i][j] = dp[i-1][j]
                else: #위가 안되면 아래쪽, 오른쪽 중 작은 것을 가져옴
                    if i+1<=n and j+1<=m:
                        dp[i][j] = min(dp[i+1][j], dp[i][j+1])
                    elif i+1<=n:
                        dp[i][j] = dp[i+1][j]
                    elif j+1<=m:
                        dp[i][j] = dp[i+1][j]
            elif dp[i-1][j] == -1:#위쪽이 물웅덩이인 경우
                if dp[i][j-1] != -1: #왼쪽을 먼저 가져오고
                    dp[i][j] = dp[i][j-1]
                else: #위가 안되면 아래쪽, 오른쪽 중 작은 것을 가져옴
                    if i+1<=n and j+1<=m:
                        dp[i][j] = min(dp[i+1][j], dp[i][j+1])
                    elif i+1<=n:
                        dp[i][j] = dp[i+1][j]
                    elif j+1<=m:
                        dp[i][j] = dp[i+1][j]
            else:
                dp[i][j] = dp[i][j-1] + dp[i-1][j]

    #for i in range(len(dp)):
    #    print(dp[i])
    answer = dp[-1][-1] % 1000000007
    return answer

if __name__ == "__main__":
    print(solution(4, 3, [[3, 3], [4, 2]])) #n은 행, m은 열