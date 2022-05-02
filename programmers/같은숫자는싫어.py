#level1 연습문제
def solution(arr):
    answer = []
    curr = -1
    for i in range(len(arr)):
        if not curr == arr[i]:
            answer.append(arr[i])
        curr = arr[i]

    return answer

if __name__ == "__main__":
    print(solution([1,1,3,3,0,1,1]))