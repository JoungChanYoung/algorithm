import heapq
def solution(scoville, K):
    answer = 0
    hq = scoville
    heapq.heapify(hq) #list -> heap
    if max(hq) < 0: return -1 #모든 원소가 0인 경우
    
    while (len(hq) > 1 and hq[0] < K):
        answer += 1
        a = heapq.heappop(hq)
        b = heapq.heappop(hq)
        tmp = a + b * 2
        heapq.heappush(hq, tmp)

    if len(hq) <= 1 and hq[0] < K: #K 보다 커질 수 없는 경우
        answer = -1

    return answer

if __name__=="__main__":
    print (solution([1, 1, 2, 2, 3, 4, 5, 6, 8,8,8], 7))