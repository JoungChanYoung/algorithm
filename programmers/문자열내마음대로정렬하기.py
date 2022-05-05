#level1 연습문제

def solution(strings, n):
    strings = sorted(strings)
    answer = []
    li = []
    for i in range(len(strings)):
        li.append([strings[i][n], i])
    
    li = sorted(li)
    for i in range(len(li)):
        answer.append(strings[li[i][1]])
    return answer


if __name__ == "__main__":
    print(solution(["abce", "abcd", "cdx"],2))