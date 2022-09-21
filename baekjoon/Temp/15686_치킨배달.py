from itertools import combinations
import copy
N, M = map(int,input().split()) #M: 폐점 시키지 않을 개수, 치킨집개수 - M: 폐점

mat = [[0 for i in range(N)]for j in range(N)]
chi_num = 0 #치킨집 개수
chi_idx = []
house = []
for i in range(N):
    tmp = input().split()
    for j in range(N):
        mat[i][j] = int(tmp[j])
        if mat[i][j] == 2:
            chi_num += 1
            chi_idx.append((i,j))
        if mat[i][j] == 1:
            house.append((i,j))

def distance(pos, obj):
    a,b = pos
    c,d = obj
    return abs(a-c) + abs(b-d)

cases = list(combinations(chi_idx, M))
visit = [[0 for i in range(N)] for j in range(N)]
result = 0
for case in cases:
    tt = 0
    di = [[0 for i in range(N)] for j in range(N)]
    for cc in case:
        a, b = cc
        for i in range(len(house)):
            c,d = house[i]
            di_tmp = distance(cc,house[i])
            if di[c][d]==0 or di[c][d] > di_tmp:
                di[c][d] = di_tmp
    aaa = 0
    for i in range(len(di)):
        aaa += sum(di[i])
    if result == 0 or aaa < result:
        result = aaa

print(result)
