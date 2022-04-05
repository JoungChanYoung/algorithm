#level3 dp
def solution(triangle):
    answer = 0
    dp = [[0 for j in range(i+1)] for i in range(len(triangle))]
    
    dp[0][0] = triangle[0][0]
    if len(triangle) < 2:
        return triangle[0][0]
    for i in range(1, len(triangle)):
        for j in range(len(triangle[i])):
            if j == 0: #맨왼쪽
                dp[i][j] = dp[i-1][j] + triangle[i][j]
            elif j == i: #맨오른쪽
                dp[i][j] = dp[i-1][j-1] + triangle[i][j]
            else: #중간
                dp[i][j] = max(dp[i-1][j] + triangle[i][j], dp[i-1][j-1] + triangle[i][j])
        answer = max(dp[-1])

    return answer

if __name__ == "__main__":
    print(solution([[7]]))