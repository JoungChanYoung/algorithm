def solution(clothes):
    di = {}
    for i, j in clothes:
        if j in di.keys():
            di[j].append(i)
        else:
            di[j] = [i]
    answer = 0
    temp = 1
    for i in di.keys():
        temp *= len(di[i]) + 1
    answer += temp - 1 #종목별로 하나씩 뽑는 경우의 수, 하나도 안입는 경우의 수 제외
    
    return answer


if __name__=="__main__":
    print (solution([["crowmask", "face"], ["bluesunglasses", "face"], ["smoky_makeup", "face"]]))