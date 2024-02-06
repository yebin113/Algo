from collections import deque

def bfs(path):
    q = deque()
    q.append(path)
    visited[path] = 1
    while q:
        path = q.popleft()
        for i in area[path]:
            if visited[i] == 0:
                visited[i] = visited[path]+1
                q.append(i)

N, M = map(int, input().split())
area = [[] for _ in range(N+1)]
for _ in range(M):
    a, b = map(int, input().split())
    area[a].append(b)
    area[b].append(a)
visited = [0]*(N+1)
bfs(1)
max_idx = visited.index(max(visited))
max_cnt = max(visited)
same_cnt = visited.count(max_cnt)
print(max_idx, max_cnt - 1, same_cnt )