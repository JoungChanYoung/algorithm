# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

stack = []
top = 0
size = 100
def push(S):
    global stack,top    
    if top>=size:
        print("error by overflow")
    else:
        stack.append(S)
        top = top + 1
    
def pop():
    global stack,top
    if top==0:
        print("empty error")
    else:
        top = top - 1
        tmp = stack[top]
        del stack[top]
        return tmp

def if_operator(a):
    global stack
    if top<2:
        return -1
    else:
        b = int(pop())
        c = int(pop())
        if a=='-':
            return b-c
        elif a =='+':
            return b+c
        elif a == '*':
            return b*c
        elif a == '/':
            return int(b/c)
        else: return False

def is_operator(S):
    if S=='-' or S=='+' or S=='*' or S=='/':
        return True
    else: return False

def if_DUPorPOP(S):
    if S == "DUP":
        push(stack[top-1])
    elif S=="POP":
        pop()
def is_DUPorPOP(S):
    if S == "DUP" or S=="POP":        
        return True
    else: return False
def solution(S):
    # write your code in Python 3.6
    S = S.split(" ")
    
    for x in range(len(S)):
        if(" " in S):
            S.remove(" ")    
    for x in range(len(S)):
        if (is_operator(S[x])):
            push(if_operator(S[x]))
        elif is_DUPorPOP(S[x]):
            if_DUPorPOP(S[x])
        else:
            push(S[x])
    return stack[top-1]    
    pass

print(solution('5 6 + -'))
