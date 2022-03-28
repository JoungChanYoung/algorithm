#level1
def solution(lottos, win_nums):
    answer = []

    count = 0
    zero_count = 0
    for i in range(len(lottos)):
        if not lottos[i]:
            zero_count += 1
        elif lottos[i] in win_nums:
            count += 1
    
    li = [0, 6, 5, 4, 3, 2] #값: 맞춘 수, index: 등수
    high, low = count+zero_count, count
    
    if high and high in li:
        answer.append(li.index(high))
    else:
        answer.append(6)
    if low and low in li:
        answer.append(li.index(low))
    else:
        answer.append(6)
    return answer

if __name__ == "__main__":
    print (solution([44, 1, 0, 0, 31, 25], [31, 10, 45, 1, 6, 19]))
    # [0, 0, 0, 0, 0, 0], 	[38, 19, 20, 40, 15, 25]