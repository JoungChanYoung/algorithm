#level1 2019 kakao blind recruitment
def solution(N, stages):
    answer = []
    li = [0 for i in range(N+1)]
    
    for i in range(len(stages)):
        li[stages[i]-1] += 1
    
    num = sum(li)
    for i in range(len(li)):
        tmp = li[i]
        if num:
            li[i] = (li[i] / num, -i)
        else:
            li[i] = (li[i], -i)
        num -= tmp

    li = sorted(li, reverse = True)
    
    for i, j in li:
        if -j != len(li)-1:
            answer.append(-j+1)
           
    return answer
if __name__ == "__main__":
    solution(4,	[4,4,4,4,4])