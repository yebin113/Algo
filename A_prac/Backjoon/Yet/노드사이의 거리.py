import sys
from collections import deque
input = sys.stdin.readline


def bfs(s,e):
    visited = [0]*N
    visited[s] = 1
    q = deque()
    q.append(s)

    while q:
        fr = q.popleft()
        for i in range(len(graph[fr])):
            t,w = graph[fr][i]
            # print(fr,t,w)
            visited[t] += visited[fr] + w
            q.append(t)
            if t == e:
                return visited[t]-1
        # print(visited)
    return 0



N,M = map(int,input().split())
graph = [[] for _ in range(N)]

# 각 인덱스에서 갈 수 있는 곳과 길이
for _ in range(N-1):
    f,t,length = map(int,input().split())
    graph[f-1].append((t-1,length))
    graph[t-1].append((f-1,length))


# 거리를 알고싶은 곳
for _ in range(M):
    start, end = map(int,input().split())
    print(bfs(start-1,end-1))
