from collections import deque
import copy
def bfs():
    global cnt,check
    q = deque()
    q.append([hx,hy,False])
    visited = [[1000000000000000]*M for _ in range(N)]
    visited[hx][hy] = 1
    while q:
        i,j,is_break = q.popleft()
        print(i,j,is_break)
        if i ==ex and j == ey:
            cnt = min(cnt,visited[i][j]-1)
            check = True
            break
        for di, dj in dir:
            ni = i + di
            nj = j + dj
            # 범위 밖
            if not (0 <= ni < N and 0 <= nj < M):
                continue
            # 최단거리 아니면 넘기기
            if visited[ni][nj] < visited[i][j] + 1:
                continue
            if maze[ni][nj] == 1 and is_break == False:
                q.append([ni,nj,True])
                visited[ni][nj] = visited[i][j] + 1
            elif maze[ni][nj] == 0:
                q.append([ni, nj, is_break])
                visited[ni][nj] = visited[i][j] + 1
        for k in range(N):
            print(maze[k],'        ',visited[k])
        print()


dir = [[0, 1], [-1, 0], [1, 0], [0, -1]]
N,M = map(int,input().split())
hx,hy = map(int,input().split())
hx -= 1
hy -= 1
ex,ey = map(int,input().split())
ex -= 1
ey -= 1
cnt = N*M
check = False
maze = []
for _ in range(N):
    maze.append(list(map(int,input().split())))
bfs()

if check:
    print(cnt)
else:
    print(-1)