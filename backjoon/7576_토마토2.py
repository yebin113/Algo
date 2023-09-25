from collections import deque
def bfs(i,j):
    visited = [[0] * M for _ in range(N)]
    visited[i][j] = 1
    end = 0
    q = deque()
    q.append((i,j))
    while q:
        i,j = q.popleft()
        for di, dj in dxy:
            ni = i + di
            nj = j + dj
            # 범위 안에 있고, 토마토가 익지 않았으며 큐에 없을때
            if 0 <= ni < N and 0 <= nj < M and tomatoes[ni][nj] == 0 and visited[ni][nj] == 0:
                # 토마토를 익게 하고, 방문표시 하고 큐에 넣기
                tomatoes[ni][nj] = 1
                visited[ni][nj] = visited[i][j] + 1
                end = visited[ni][nj]
                q.append((ni,nj))
    return end


# M은 상자의 가로 칸의 수, N은 상자의 세로 칸
M, N = map(int, input().split())
# 정수 1은 익은 토마토, 정수 0은 익지 않은 토마토, 정수 -1은 토마토가 들어있지 않은 칸
tomatoes = [list(map(int, input().split())) for _ in range(N)]
day = 0

dxy = [[0, -1], [-1, 0], [0, 1], [1, 0]]

# 저장될 때부터 모든 토마토가 익어있는 상태이면 0을 출력해야 하고
flag = True
flag2 = True

for i in range(N):
    # 익은 토마토가 없는 경우 체크
    if tomatoes[i].count(1) != 0:
        flag = False
        break
for i in range(N):
    # 안익은 토마토가 없는 경우 체크
    if tomatoes[i].count(0) != 0:
        flag2 = False
        break
# 익은 토마토가 없다면 익을 수 없음..
if flag:
    day = -1
elif flag2:
    day = 0
else:
    day = 0
    start = []
    for i in range(N):
        for j in range(M):
            if tomatoes[i][j] == 1:
                start.append((i,j))
    for i,j in start:
        end = bfs(i,j)
        # 더 오래 걸리는 날 갱신
        if day < end:
            day = end


    # 만약 다 했는데 못익은 토마토가 존재하면..
    for i in range(N):
        # 안익은 토마토 존재???
        if tomatoes[i].count(0) != 0:
            day = -1
            break

# 토마토가 모두 익을 때까지의 최소 날짜
print(day)
