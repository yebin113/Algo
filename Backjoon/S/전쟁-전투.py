dxy = [[0,-1],[-1,0],[1,0],[0,1]]
from collections import deque
def dfs(i,j,team):
    path.append((i,j))
    visit[i][j] = 1
    for di,dj in dxy:
        ni = i + di
        nj = j + dj
        if 0<=ni<N and 0<=nj<M and visit[ni][nj]==0 and arr[ni][nj]==team:

            dfs(ni,nj,team)
    return len(path)


import sys
M,N = map(int,sys.stdin.readline().split())
arr = deque()
for _ in range(N):
    arr.append(list(map(str,sys.stdin.readline().strip())))
pointW = 0
pointB = 0

visit= [[0]*M for _ in range(N)]
for i in range(N):
    for j in range(M):
        if visit[i][j] != 0:
            continue
        path = deque()
        point = dfs(i, j,arr[i][j]) ** 2
        if arr[i][j]=='W':
            pointW += point
        else:
            pointB += point
print(pointW,pointB)
