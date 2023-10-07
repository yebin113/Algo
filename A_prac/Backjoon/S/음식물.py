import sys
from collections import deque
def bfs(i,j):
    visit = [[0] * M for _ in range(N)]
    out = 0
    q = deque()
    q.append((i,j))
    visited[i][j]=1
    visit[i][j] = 1

    while q:
        i,j = q.popleft()
        for di,dj in dxy:
            ni = i+di
            nj=j+dj
            if 0<=ni<N and 0<=nj<M and arr[ni][nj]==1 and visit[ni][nj]==0:
                q.append((ni,nj))
                visit[ni][nj] = 1
    for k in range(N):
        for m in range(M):
            if visit[k][m] ==0:
                continue
            out += 1
    return out


dxy = [[0, -1], [-1, 0], [0, 1], [1, 0]]
# 세로 길이 N과 가로 길이 M 그리고 음식물 쓰레기의 개수 K
N, M, K = map(int, sys.stdin.readline().split())
arr = [[0] * M for _ in range(N)]
# K개의 줄에 음식물이 떨어진 좌표 (r, c)
for _ in range(K):
    r, c = map(int, sys.stdin.readline().split())
    r -= 1
    c -= 1

    arr[r][c] = 1
max_size = 0
visited = [[0] * M for _ in range(N)]
for i in range(N):
    for j in range(M):
        if arr[i][j] != 0 and visited[i][j] == 0:
            max_size=max(bfs(i,j),max_size)



print(max_size)
