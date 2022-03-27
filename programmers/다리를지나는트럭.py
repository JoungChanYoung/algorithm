from collections import deque
def solution(bridge_length, weight, truck_weights):
    answer = 0

    truck_num = len(truck_weights)
    bridge = deque([0 for i in range(bridge_length)])
    
    count = 0

    bridge_weight = sum(bridge)
    while(truck_weights or bridge_weight != 0):
        count += 1              
        if bridge[-1]: #다리 맨끝에 있는 트럭이 다리를 통과
            bridge_weight -= bridge.pop()        
            bridge.appendleft(0)            
        else:  #다리 맨끝에 트럭이 없는 경우
            tmp = bridge.pop()
            bridge.appendleft(tmp)
            bridge_weight += tmp
        
        if truck_weights: #다리 못올라온 트럭이 남아 있는 경우
            curr = truck_weights[0]
            if (bridge_weight + curr > weight): #다리 총무게 때문에 안되는 경우
                continue
            else: #되는 경우
                bridge[0] = truck_weights.pop(0)
                bridge_weight += bridge[0]
    answer = count
    return answer

if __name__ == "__main__":
    print (solution(2, 10, [7,4,5,6]))