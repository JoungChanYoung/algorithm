#level1 
def solution(arr, divisor):
    answer = []
    arr = sorted(arr)

    for i in range(len(arr)):
        if arr[i] % divisor == 0:
            answer.append(arr[i])
    
    if not answer:
        return [-1]
    return answer

if __name__ == "__main__":
    print(solution([5, 9, 7, 10], 5))