'''

'(' or ')' 으로 괄호검사

'''

def check(li):
    global stack,top
    for x in range(len(li)):
        if li[x] == ')':
            if top == 0: #empty
                return False            
            stack.pop(top-1)
            top = top - 1
        else:
            stack.append(li[x])
            top = top + 1
    if (top == 0):
        return True
    else: return False
            
input_num = int(input())

arr = []

for x in range (input_num):
    arr.append(input())

for x in range (len(arr)):
    stack = []
    top = 0
    tmp = arr[x]
    if check(tmp):
        print("YES")
    else: print("NO") 



