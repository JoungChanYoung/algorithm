#level2 2020 kakao blind recruitment
from collections import deque
    
def balanced(p):
    s = deque() #stack
    for i in range(len(p)):
        tmp = p[i]
        if s and (s[-1] == '(' and tmp == ')'):
            s.pop()
        else:
            s.append(p[i])
    if not s:
        return True

def func(p):
    if p == "":
        return ""
    u = ''
    v = ''
    check = [0, 0] # () check
    for i in range(len(p)):
        if p[i] == "(":
            check[0] += 1
        else:
            check[1] += 1
        if check[0] and check[1] and check[0] == check[1]:
            u = p[:i+1]
            v = p[i+1:]
            break
    if balanced(u):
        return u + func(v)
    else:        
        tmp = '(' + func(v) + ')'
        tmp2 = u[1:-1]
        tmp3 = ''
        for i in tmp2:
            if i == '(':
                tmp3 += ')'
            else:
                tmp3 += '('        
        return tmp + tmp3

def solution(p):
    answer = ''    
    if balanced(p):
        return p
    else:
        return func(p)
    
    return answer

if __name__ == "__main__":
    print(solution("()()"))