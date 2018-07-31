''' example input
5 6
1
5 1 1
1 2 2
1 3 3
2 3 4
2 4 5
3 4 6
'''
from collections import deque
import heapq
import sys
#V : num of vertex , E : num of edge
V,E = map(int,input().split())
start_vertex = int(input())

#dictonary init
a = {}
for x in range(V):
    a[x+1] = {}

# #input
for num in range(E):
    u, v, w = map(int,sys.stdin.readline().split())
    if v in a[u].keys():
        if a[u].get(v) <= w:
            continue
    #dict추가에는 update 사용
    a[u].update({v : w})
#print(a)
visited = [0 for x in range(V+1)]
cost = [1000000007 for x in range(V+1)] # start_vertex에서 index까지의 cost

cost[start_vertex] = 0
pq = []
for k,v in a[start_vertex].items():
    heapq.heappush(pq,(v,start_vertex))

while pq:
    #priority변수는 우선순위 heapq을 루프를통해 사용하기위해 넣음 사용되진 않음
    priority, vertex = heapq.heappop(pq) #heappop은 heap에서 우선순위 가장낮은것 부터 출력
    visited[vertex] = True
    for key in a[vertex].keys():
        if visited[key] ==True: #방문했던 vertex에 접근할경우 continue
            continue
        #저장된값이 새로운값보다 크면 갱신
        if cost[key] > a[vertex].get(key) + cost[vertex]:
            cost[key] = a[vertex].get(key) + cost[vertex]
            heapq.heappush(pq,(cost[key],key)) #pq에 우선순위,다음vertex값(cost[key],key) 삽입

for x in range(V):
    if cost[x+1] >= 1000000007:
        print('INF')
    else:
        print(cost[x+1])
