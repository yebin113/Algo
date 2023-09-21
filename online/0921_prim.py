"""
7 11
0 1 32
0 2 31
0 5 60
0 6 51
1 2 21
2 6 25
2 4 46
3 4 34
3 5 18
4 5 40
4 6 51
"""

import heapq
def prim(start):
    heap = []
    # 우선순위에 따라(오름차순)으로 만들어줌
    # 가중치, 접점정보
    heapq.heappush(heap,(0,start))
    MST = [0]*V
    sum_w = 0
    while heap:
        #
        weight, v = heapq.heappop(heap)
        # 방문했던 노드라면 pass
        if MST[v]:
            continue
        # 방문 처리
        MST[v] = 1
        sum_w += weight
        # 갈 수 있는 노드라면
        for next in range(V):
            # 갈 수 없거나 이미 방문했다면
            if graph[v][next] == 0 or MST[next]:
                continue
            heapq.heappush(heap,(graph[v][next], next))
    return sum_w


V, E = map(int,input().split())
# 인접 행렬
graph = [[0] * V for _ in range(V)]

for _ in range(E):
    f,t,w = map(int,input().split())
    graph[f][t] = w
    graph[t][f] = w     # 무방향 그래프
print(prim(0))