
from collections import deque
q = deque()
 # node의 개수는 최대 32000개
inDegree = [0 for x in range(32001)]
result = [0 for x in range(32001)]
#edge는 노드번째 연결된 간선 정보 저장
# ex) [[0], [5] ...] : 1번째 노드에 5가 연결(1번째 노드가 5를 가리킴)
edge = [[0] for x in range(32001)]

def topologySort(n): # n : 학생 수
    q = deque() # 큐생성
    for x in range(n):
        # 진입차수가 0인 노드 검색해서 q에삽입
        if inDegree[x+1] == 0: #인덱싱문제때문에 x+1사용
            q.append(x+1)
    for i in range(n):
        tmp = q.popleft()
        tmp2 = 0
        # 개행문자 없이 출력(end = " ")
        print(tmp,end=" ")
        if edge[tmp][0]:
            #edge의 tmp번째 값들을 불러와서 그에 맞는 inDegree[인덱스] 값을 낮춰줌
            #그 후 진입차수가 0이된 노드를 q에 다시 삽입
            for y in range(len(edge[tmp])):
                tmp2 = edge[tmp][y]
                inDegree[tmp2] -= 1
                if inDegree[tmp2] == 0:
                    q.append(tmp2)


# N : 학생 수(node의개수), M : 키 비교 회수(dege의개수)
# inDegree : 진입차수(연결된 edge의 개수)
N,M = map(int,input().split())
for y in range(M):
    s = input().split()
    upper = int(s[0])
    lower = int(s[1])
    inDegree[lower] += 1 #진입차수 증가
    if edge[upper][0] == 0: #edge 벡터 비어있을때
        edge[upper] = [lower]
    else : #edge 벡터 값 있을때
        edge[upper].append(lower)
# print('inDegree : ',inDegree[0:10])
# print('edge : ',edge[0:10])
topologySort(N)
