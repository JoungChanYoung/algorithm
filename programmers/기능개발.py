from collections import deque 
def solution(progresses, speeds):
    speeds = deque(speeds)
    curr = deque(progresses)
    answer = []
    
    while(curr):  
        tmp = 0              
        for i in range(len(speeds)):
            curr[i] += speeds[i]
        if curr[0] >= 100:            
            while(curr and curr[0] >= 100):                
                curr.popleft()   
                speeds.popleft()  
                tmp += 1
        if tmp != 0:
            answer.append(tmp)
    return answer

if __name__ == "__main__":
    print (solution([95, 90, 99, 99, 80, 99], [1, 1, 1, 1, 1, 1]))
