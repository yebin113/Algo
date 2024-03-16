from collections import deque
import heapq
def dj(start,end):
    heap = [[0,start]]
    visited = [1000000000]*(N+1)
    visited[start] = 0
    while heap:
        # print(heap)
        w, i = heapq.heappop(heap)
        if i == end:
            return w
        for ni, nw in graph[i]:
            if visited[ni] <= w + nw:
                continue
            visited[ni] = w + nw
            heapq.heappush(heap,[w+nw,ni])

# def bfs(start,end):
#     q = deque()
#     q.append([start,0])
#     while q:
#         i,w = q.popleft()
#         # for nw, ni in graph[i]:

N,M = map(int,input().split())
graph = [[] for _ in range(N+1)]
for _ in range(M):
    a,b,c = map(int,input().split())
    graph[a].append([b, c])
    graph[b].append([a, c])

s, t = map(int,input().split())
print(dj(s,t))
