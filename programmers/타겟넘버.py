#level2 dfs
def dfs(numbers, idx, target, curr_num, answer):
    if idx == len(numbers):
        if target == curr_num:
            answer += 1
        return answer    

    answer = dfs(numbers, idx+1, target, curr_num+numbers[idx], answer)
    answer = dfs(numbers, idx+1, target, curr_num-numbers[idx], answer)
            
    return answer

def solution(numbers, target):
    answer = 0
    answer = dfs(numbers, 0,target, 0, answer)
    return answer

if __name__ == "__main__":
    print (solution([4, 1, 2, 1], 4))