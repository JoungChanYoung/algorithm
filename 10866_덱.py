from collections import deque

deq = deque()

test_case = int(input())

def is_empty():
    if deq:
        return 0
    else:
        return 1
for x in range(test_case):
    order = input().split()
    if order[0] == 'push_front':
        deq.appendleft(int(order[1]))
    elif order[0] == 'push_back':
        deq.append(int(order[1]))
    elif order[0] == 'empty':
        print(is_empty())
    elif order[0] == 'size':
        print(len(deq))
    else:
        if is_empty():
            print(-1)
        elif order[0] == 'pop_front':
            print(deq.popleft())
        elif order[0] == 'pop_back':
            print(deq.pop())
        elif order[0] == 'front':
            print(deq[0])
        elif order[0] == 'back':
            print(deq[-1])
