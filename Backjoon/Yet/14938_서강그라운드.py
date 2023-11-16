import heapq
from collections import deque
from heapq import heappush, heappop, heapify


def bfs(x):
    q = [[0, x]]
    visited= [int(1e9)]*n
    visited[x] = 0
    while q:
        dis, now = heappop(q)
        # 반복문에서 다음과 다음 가중치, 지나온 길을 받음
        for next,next_dis in graph[now]:
            if next_dis + dis < visited[next]:

                visited[next] = next_dis + dis
                heapq.heappush(q,[next_dis + dis,next])
    return visited


n, m, r = map(int, input().split())
item = list(map(int, input().split()))
graph = [[] for _ in range(n)]

for i in range(r):
    a, b, l = map(int, input().split())
    # 다음 위치와 가중치
    graph[a - 1].append([b - 1, l])
    graph[b - 1].append([a - 1, l])
#     print(graph)
# print('graph', graph)
max_item = 0
for i in range(n):
    item_count = 0
    now_item = bfs(i)
    for j in range(n):
        if now_item[j] <= m:
            item_count += item[j]

    max_item = max(max_item, item_count)
print(max_item)
