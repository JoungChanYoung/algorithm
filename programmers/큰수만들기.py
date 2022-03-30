#level2 greedy
def solution(number, k):
    answer = ''
    
    stack = []
    for num in number:
        while k > 0 and stack and stack[-1] < num:
            stack.pop()
            k -= 1
        stack.append(num)
    
    answer = "".join(stack[:len(stack)-k])
    return answer

if __name__ == "__main__":
    print(solution("765432",2))