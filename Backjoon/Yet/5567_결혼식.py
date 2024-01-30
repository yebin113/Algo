from collections import deque
N = int(input())
M = int(input())
graph = [[] for _ in range(N+1)]
visited = [0]*(N+1)
for _ in range(M):
    a,b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)



q = deque()
for num in graph[1]:
    visited[num] = 1
    if num not in q:
        q.append(num)

while q:
    num = q.popleft()
    for n in graph[num]:
        visited[n] = 1

visited[1] = 0
print(visited.count(1))