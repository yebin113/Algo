from collections import deque
from heapq import heappush, heappop, heapify


def bfs(x):
    item_count = item[x]
    q = [[0, x]]
    visited= [0]*n
    while q:
        dis, now = heappop(q)
        # 반복문에서 다음과 다음 가중치, 지나온 길을 받음
        for next, next_dis in graph[now]:
            if next_dis + dis > m or visited[next] != 0:
                continue
            item_count += item[next]
            visited[next] = 1
            heappush(q, [dis + next_dis, next])
        # print(f'now {now} graph[now] {graph[now]} q {q}')
    return item_count


n, m, r = map(int, input().split())
item = list(map(int, input().split()))
graph = [[] for _ in range(n)]

for i in range(r):
    a, b, l = map(int, input().split())
    # 다음 위치와 가중치
    graph[a - 1].append((b - 1, l))
    graph[b - 1].append((a - 1, l))
#     print(graph)
# print('graph', graph)
max_item = 0
for i in range(n):
    now_item = bfs(i)
    max_item = max(max_item, now_item)
print(max_item)
