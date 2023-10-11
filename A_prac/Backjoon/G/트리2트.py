

from sys import stdin
from collections import deque
def bfs(i):
    cycle = False
    q = deque()
    q.append(i)

    while q:
        now = q.popleft()
        if visited[now]:
            cycle = True
            # return cycle
        visited[now] = 1
        for next in graph[now]:
            if visited[next] ==0:
                q.append(next)
    return cycle
cnt = 0
while True:
    cnt += 1
    n,m = map(int,stdin.readline().split())
    if n == 0 and m==0:
        break

    graph = [[0]*(n+1) for _ in range(n+1)]
    check  = False
    for _ in range(m):
        f,t = map(int,stdin.readline().split())
        graph[f][t] = 1
        graph[t][f] = 1
    visited= [0]*(n+1)
    tree = 0
    for node in range(1,n+1):
        if visited[node] ==0:
            if not bfs(node):
                tree += 1


    print(f'Case {cnt}:',end=' ')
    if tree==0:
        print('No trees.')
    elif tree > 1:
        print(f'A forest of {tree} trees.')
    elif tree==1:
        print('There is one tree.')

