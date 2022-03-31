#level1 
def solution(numbers):
    answer = 0

    li = [0 for i in range(10)]
    for i in range(len(numbers)):
        li[numbers[i]] = 1
    
    for i in range(len(li)):
        if not li[i]:
            answer += i
    return answer

if __name__ == "__main__":
    print(solution([1,2,3,4,6,7,8,0]))