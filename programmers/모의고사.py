def solution(answers):
    answer = []
    pattern1 = [1,2,3,4,5]
    pattern2 = [2,1,2,3,2,4,2,5]
    pattern3 = [3,3,1,1,2,2,4,4,5,5]
    a = b = c = 0
    for i in range(len(answers)):
        if answers[i] == pattern1[i % len(pattern1)]:
            a += 1
        if answers[i] == pattern2[i % len(pattern2)]:
            b += 1
        if answers[i] == pattern3[i % len(pattern3)]:
            c += 1

    result = [a,b,c]
    max_num = max(result)
    first = 0
    
    for i in range(len(result)):
        if max_num == result[i]:
            answer.append(i+1)
    answer.sort()
    return answer
if __name__ == "__main__":
    print (solution([2,1,2,3,2,4,2,5]))