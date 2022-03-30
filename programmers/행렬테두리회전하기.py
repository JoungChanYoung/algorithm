#level2 2021-dev-matching
def solution(rows, columns, queries):
    answer = []
    
    li = [[0 for j in range(columns)] for i in range(rows)]

    tmp = 0
    for i in range(rows):
        for j in range(columns):
            tmp += 1
            li[i][j] = tmp

    for x1, y1, x2, y2 in queries:
        tmp = li[x1-1][y1-1]
        min_num = tmp

        for i in range(x1-1, x2-1):
            t = li[i+1][y1-1]
            li[i][y1-1] = t
            min_num = min(min_num, t)
        
        for i in range(y1-1,y2-1):
            t = li[x2-1][i+1]
            li[x2-1][i] = t
            min_num = min(min_num, t)

        for i in range(x2-1,x1-1,-1):
            t = li[i-1][y2-1]
            li[i][y2-1] = t
            min_num = min(min_num, t)

        for i in range(y2-1,y1-1,-1):
            t = li[x1-1][i-1]
            li[x1-1][i] = t
            min_num = min(min_num, t)
        
        li[x1-1][y1] = tmp
        answer.append(min_num)
    return answer

if __name__ == "__main__":
    print(solution(3, 5, [[1, 1, 2, 2], [2, 3, 3, 4], [1, 2, 3, 4], [1, 1, 3, 4], [2, 2, 3, 5]]  ))
    