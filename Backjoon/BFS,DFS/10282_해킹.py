import sys
from collections import deque
input = sys.stdin.readline

def bfs(n,c):
    warm = [0] * (n + 1)
    q = deque()
    warm[c] = 1
    q.append(c)

    while q:
        fr = q.popleft()
        # print(graph)
        # print(warm)
        # print()
        for to, time in graph[fr]:
            if warm[to] != 0 and warm[to] < warm[fr] + time:
                continue
            warm[to] = warm[fr] + time
            q.append(to)

    return n - warm.count(0)+1, max(warm)-1


T = int(input())


for _ in range(T):
    n,d,c = map(int,input().split())
    graph = [[] for _ in range(n+1)]

    for _ in range(d):
        a,b,s = map(int,input().split())
        graph[b].append([a,s])
    print(*bfs(n,c))
