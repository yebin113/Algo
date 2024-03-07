from collections import deque
import copy
def bfs(arr,i,j):
    global cnt,check
    q = deque()
    q.append([i,j])
    visited = [[0]*M for _ in range(N)]
    visited[i][j] = 1
    while q:
        i,j = q.popleft()
        if i ==ex and j == ey:
            cnt = min(cnt,visited[i][j]-1)
            check = True

            break
        for di, dj in dir:
            ni = i + di
            nj = j + dj
            if not (0 <= ni < N and 0 <= nj < M) or arr[ni][nj] == 1 or visited[ni][nj] != 0:
                continue
            q.append([ni,nj])
            visited[ni][nj] = visited[i][j] + 1
    # for k in range(N):
    #     print(visited[k])
    # print()

def is_right(i,j):
    cnt = 0
    for di, dj in dir:
        ni = i + di
        nj = j + dj
        if not (0 <= ni < N and 0 <= nj < M) or maze[ni][nj] == 1:
            cnt += 1
            continue
    if cnt >= 3:
        return False
    return True

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

for i in range(N):
    for j in range(M):
        if maze[i][j] == 1 and is_right(i,j):
            arr = copy.deepcopy(maze)
            arr[i][j] = 0
            bfs(arr,hx,hy)
            # maze[i][j] = 1
if check:
    print(cnt)
else:
    print(-1)