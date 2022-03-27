def solution(n, lost, reserve):
    answer = 0
    answer = n - len(lost)

    reserve.sort()
    lost.sort()

    li = []
    for i in range(len(lost)):
        if lost[i] in reserve:
            reserve.remove(lost[i])
            answer += 1
            li.append(lost[i])

    for i in li:
        lost.remove(i)
           
    for i in range(len(lost)):
        if (lost[i] - 1) in reserve:
            reserve.remove(lost[i] - 1)
            answer += 1  
        elif (lost[i] + 1) in reserve:
            reserve.remove(lost[i] + 1)
            answer += 1                    
       
    return answer

if __name__ == "__main__":
    print(solution(6,[1,3,6],[1,3,7]))