def solution(n, arr1, arr2):
    answer = []
    for i in range(n):
        answer.append(bin(arr1[i]|arr2[i]))
    for i in range(n):
        tmp = answer[i].split('0b')[-1]
        if len(tmp) < n:
            t = n - len(tmp) #개 만큼 0을 앞에다 붙이기
            for _ in range(t):
                tmp = '0' + tmp
        tmp = tmp.replace('1','#')
        tmp = tmp.replace('0',' ')
        answer[i] = tmp
    return answer

arr1 = [46, 33, 33 ,22, 31, 50]
arr2 = [27 ,56, 19, 14, 14, 10]
print(solution(6,arr1,arr2))
