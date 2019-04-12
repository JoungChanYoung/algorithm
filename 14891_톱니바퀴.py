gear = [[0 for i in range(8)] for j in range(4)]
for i in range(4):
    tmp = input()
    for j in range(8):
        gear[i][j] = int(tmp[j])

tc = int(input())

def turn(ge, di): #(gear[n], direction)
    if di == 1: #시계
        pass
        tmp = ge.pop()
        ge.insert(0,tmp)
    elif di == -1:
        tmp = ge[0]
        del(ge[0])
        ge.append(tmp)
    return ge

for _ in range(tc):
    gear_num, dir = map(int, input().split()) #dir == 1 -> 시계
    gear_num = gear_num-1
    q = []
    q.append((gear_num,dir))
    visit = [0 for i in range(4)]
    to_turn = []
    to_turn.append((gear_num,dir))
    while(q):
        i,dd = q.pop()
        if visit[i] == 1:
            continue
        visit[i] = 1
        if i < 3 and not gear[i][2] == gear[i+1][-2]: #오른쪽거 회전
            if not visit[i+1]:
                to_turn.append((i+1, dd * (-1)))
                q.append((i+1, dd * (-1)))
        if i > 0 and not gear[i][-2] == gear[i-1][2]: #왼쪽회전
            if not visit[i-1]:
                to_turn.append((i-1, dd * (-1)))
                q.append((i-1, dd * (-1)))
    for j in range(len(to_turn)):
        a,b = to_turn[j]
        turn(gear[a],b)
result = 0 #최종
for i in range(4):
    result += gear[i][0] * pow(2,i)

print(result)
