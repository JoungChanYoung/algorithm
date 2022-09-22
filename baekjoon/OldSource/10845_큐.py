
#큐구현 , 명령 처리
'''
예제 입력

15
push 1
push 2
front
back
size
empty
pop
pop
pop
size
empty
pop
push 3
empty
front

'''

test_case = int(input())

order = []
for x in range(test_case):
    order.append(input())
queue = []
front = 0
rear = 0

def push(x):
    global queue,front,rear
    rear += 1
    queue.append(x)

def pop():
    global queue,front,rear
    if is_empty():
        return -1
    else:
        front_tmp = front
        queue_tmp = queue[front]
        front += 1
        return int(queue_tmp)

def is_empty():
    global queue,front,rear
    return int(rear==front)

def check_front():
    global queue,front,rear
    if is_empty():
        return -1
    else:
        return int(queue[front])

def check_back():
    global queue,front,rear
    if is_empty():
        return -1
    else:
        return int(queue[-1])

def size():
    if is_empty():
        return 0
    else:
        return (len(queue[front:]))

for x in range(len(order)):
    # print('order[x]',order[x],'queue',queue,'rear',rear,'front',front)
    if "push" in order[x]:
        push(order[x].split(" ")[-1])

    elif order[x] == "pop":
        print(pop())

    elif order[x] == "front":
        print(check_front())

    elif order[x] == "empty":
        print(is_empty())

    elif order[x] == "size":
        print(size())

    elif order[x] == "back":
        print(check_back())
