def solution(priorities, location):
    answer = 0
    while(priorities):
        max_num = max(priorities)
        num = priorities.pop(0)

        if max_num == num:
            answer += 1
            if location == 0:
                break
            else:
                location -= 1
            
        else:
            priorities.append(num)
            if location==0:
                location = len(priorities) - 1
            else:
                location -= 1
    return answer

        
if __name__ == "__main__" :
    print (solution([1, 1, 9, 1, 1, 1], 2))