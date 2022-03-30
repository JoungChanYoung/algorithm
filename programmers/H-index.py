#level2
def solution(citations):
    answer = 0
    
    cnt = 1
    citations.sort(reverse=True)
    for i in range(len(citations)):        
        h = citations[i]
        if cnt == h:
            answer = cnt
            break
        elif cnt > h:
            answer = cnt-1
            break
        elif cnt < h and cnt == len(citations): #마지막 수인 경우
            answer = cnt
        cnt += 1

    return answer

if __name__ == "__main__":
    print (solution([10, 10, 10, 10, 10])) #h-index: 5
