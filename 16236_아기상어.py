from collections import deque
import copy
N = int(input())
mat = [[0 for i in range(N)] for j in range(N)]
fi = deque()
pos = None
shark = 2
for i in range(N):
    tmp = input().split()
    for j in range(N):
        t = int(tmp[j])
        if t == 9:
            pos = (i,j) #초기 상어 위치 저장, 상어는 1마리
        mat[i][j] = t
tttt = []
for i in range(N):
    for j in range(N):
        if mat[i][j] == 1:
            tttt.append((i,j))
visit_t = [[0 for i in range(N)] for j in range(N)]

def find(mat, ss, r, c, obr, obc,visit):
    q = deque()
    q.append((r,c,0))
    distance = 0
    ff = 0
    if visit[obr][obc] is not 0:
        return visit[obr][obc]
    while(q): #찾아갈때까지
        a, b, di = q.popleft()
        if visit[a][b] is not 0:
            continue
        if a == obr and b == obc:
            ff = 1
            break
        if a + 1 <= N-1 and ss >= mat[a+1][b]:
            q.append((a+1,b,di+1))
        if b + 1 <= N-1 and ss >= mat[a][b+1]:
            q.append((a,b+1,di+1))
        if a - 1 >= 0 and ss >= mat[a-1][b]:
            q.append((a-1,b,di+1))
        if b - 1 >= 0 and ss >= mat[a][b-1]:
            q.append((a,b-1,di+1))

        if di == 0 :
            visit[a][b] = di+1
        else:
            visit[a][b] = di
    if ff == 1:
        distance = di
    else:
        distance = -1
    return distance

a,b = pos
kkk = []
visit = copy.deepcopy(visit_t)
for i in range(len(tttt)):
    aa,bb=tttt[i]
    dis = find(mat, shark, a, b, aa, bb,visit)
    if dis > 0:
        kkk.append((dis,aa,bb))
aaa = bbb = -1
kkk = sorted(kkk)
if kkk:
    ccc,aaa,bbb = kkk[0]
if aaa is not -1:
    fi.append((aaa,bbb))

res = 0
def func(mat,r,c):
    global shark,res

    cnt = 0
    ccccc = 0
    while(fi):
        #print(fi)
        a, b  = fi.popleft()
        flag = 0
        for i in range(N):
            for j in range(N):
                if shark - 1 >= mat[i][j] and mat[i][j] is not 0:
                    flag = 1
                    break

        if flag == 0:
            break
        #print(mat, shark, r, c, a, b,res)
        visit = copy.deepcopy(visit_t)
        ddd = find(mat, shark, r, c, a, b,visit)
        if ddd == -1:
            continue
        mat[a][b] = 0
        r = a
        c = b
        res += ddd
        cnt += 1
        if shark == cnt:
            shark += 1
            cnt = 0

        ttt=[]
        for i in range(N):
            for j in range(N):
                if shark-1 >= mat[i][j] and mat[i][j] is not 0:
                    ttt.append((i,j))
        #print(ttt)
        kkk = []
        di = 0
        visit = copy.deepcopy(visit_t)
        for i in range(len(ttt)):
            aa,bb=ttt[i]
            di = find(mat, shark, r, c, aa, bb,visit)
            if di > 0:
                kkk.append((di,aa,bb))
        #print(kkk)
        kkk = sorted(kkk)
        #print(kkk)
        aaa = bbb = -1
        if kkk:
            ccc, aaa, bbb = kkk[0]
        if aaa == -1:
            continue
        fi.append((aaa,bbb))
r,c = pos
mat[r][c] = 0
func(mat,r,c)
print(res)
