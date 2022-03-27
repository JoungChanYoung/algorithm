def solution(numbers):
    answer = ''

    if sum(numbers) == 0:
        return '0'
    
    li = []
    for number in numbers: #number 하나로 만들 수 있는 네 자리 수 끼리 비교
    # 예를 들어, 3 -> 3333, 32 -> 3232. 따라서 3이 32보다 우선되야한다.
        tmp = (str(number) * 4)[:4]
        num_len = len(str(number))
        li.append((tmp, num_len))
    li.sort(reverse=True)

    for tmp, num_len in li:
        answer += tmp[:num_len]
    return answer

if __name__ == "__main__":
    print(solution([6, 10, 2])) #숫자 조합 중 가장 큰 숫자 조합 string으로 출력
    #숫자는 1000이하로 주어짐