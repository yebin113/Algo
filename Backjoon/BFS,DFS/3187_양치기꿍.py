from collections import deque

def bfs(i,j):
    q=deque()
    q.append((i,j))
    cnt_yang = 0
    cnt_nd = 0
    visited[i][j] = 1

    if area[i][j] == 'v':
        cnt_nd += 1
    elif area[i][j] == 'k':
        cnt_yang += 1

    while q:
        x,y = q.popleft()
        for dx, dy in dir:
            nx = x+dx
            ny = y+dy
            # 범위 밖이거나 벽이면 패스
            if not(0<=nx<R and 0<=ny<C) or area[nx][ny] =='#' or visited[nx][ny] != 0:
                continue
            if area[nx][ny] == 'v':
                cnt_nd += 1
            elif area[nx][ny] == 'k':
                cnt_yang += 1
            q.append((nx,ny))
            visited[nx][ny] = 1
    if cnt_yang > cnt_nd:
        res[0] += cnt_yang
    else:
        res[1] += cnt_nd





# 빈 공간을 '.'
# 울타리를 '#',
# 늑대를 'v',
# 양을 'k'

R,C = map(int,input().split())
dir = [[0, 1], [-1, 0], [1, 0], [0, -1]]
area = []
res = [0,0]
for _ in range(R):
    area.append(list(input()))
visited = [[0]*C for _ in range(R)]
for i in range(R):
    for j in range(C):
        if visited[i][j] != 0 or area[i][j] =='#':
            visited[i][j] = 1
            continue
        bfs(i,j)

print(*res)