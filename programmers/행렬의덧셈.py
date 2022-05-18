#level1 

def solution(arr1, arr2):
    answer = []    
    for i, j in zip(arr1, arr2):
        tmp = []
        for k, p in zip(i, j):
            tmp.append(k+p)
        answer.append(tmp)
    return answer

if __name__ == "__main__":
    print(solution([[1,2],[2,3]], [[3,4],[5,6]]))