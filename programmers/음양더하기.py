#level1 월간 코드 챌린지 시즌2
def solution(absolutes, signs):
    print(signs)
    answer = 0
    for i in range(len(signs)):
        if signs[i]:
            answer += absolutes[i]
        else:
            answer -= absolutes[i]
    
    return answer

if __name__ == "__main__":
    print(solution([4,7,12],	[True,False,True]))