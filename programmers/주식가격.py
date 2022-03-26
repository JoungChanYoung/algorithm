from collections import deque
def solution(prices):
    deq = deque(prices)
    answer = []

    while (deq):
        sec = 0
        price = deq.popleft() 
        for q in deq:
            sec += 1
            if price > q:
                break
        answer.append(sec)
    return answer

if __name__=="__main__":
    print(solution([1, 3, 5, 7, 9, 4, 5, 2, 1, 0])) #[9, 6, 3, 2, 1, 2, 1, 1, 1, 0]