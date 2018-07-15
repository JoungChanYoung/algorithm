#상자에 무작위로 토마토가 있음.
#0 : 덜익은토마토, 1 : 다익은토마토, -1 : 빈칸
#하루에 다익은토마토 인접(대각선제외)한 토마토 익음.
'''
#example input
6 4
0 0 0 0 0 0
0 0 0 0 0 0
0 0 0 0 0 0
0 0 0 0 0 1
'''
from collections import deque

flag = 0
def bfs(graph, start_point, box_row, box_col): #graph는 2차원 배열 형태
    global flag
    j = i = 0
    day = [[0]*box_col for x in range(box_row)]
    while start_point: #start_point는 queue의 형태
        n = start_point.popleft()
        j,i = n[0],n[1]
        for y,x in (j+1,i),(j,i+1),(j-1,i),(j,i-1):
            if 0<=y<box_row and 0<=x<box_col:
                if graph[y][x]:
                    continue
                graph[y][x] = 1
                day[y][x] = day[j][i] + 1
                start_point += [[y,x]]
                flag -= 1
    if flag:
        return -1
    return day[j][i]

q = deque()
box_size = input().strip().split()
col, row = int(box_size[0]) , int(box_size[1])
tomato = [[-1]*1000 for x in range(1000)]

for y in range(row):
    val = input().strip().split()
    for x in range(col):
        tomato[y][x] = int(val[x])
        if int(val[x]) == 1: #1들어간 인덱스 start_point에 저장
            q+=[[y,x]]
        elif not int(val[x]): #0일때의 개수
            flag += 1

#토마토가 다 익어있으면 0 출력(입력에 1 or -1만 있는 경우)
#토마토가 다 익을수 없는상황이면 -1 출력
#토마토가 다익는 일 수 출력
print(bfs(tomato, q, row, col))
