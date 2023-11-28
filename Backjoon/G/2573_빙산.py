from sys import stdin
from collections import deque

"""
bfs에서는 얼음이 번진 범위와 다음에 얼마나 녹을지 세는 cnt를 조작함
while문을 돌면서 bfs에서 구한 얼음이 아닌곳의 구간들을 빼서 얼음을 깎아줘야함
하지만 for문을 돌면서 바로 제거한다면, 다음 얼음에 영향을 미칠것
따라서 bfs를 돌려주는 for문과 얼음을 깎는 for문 두개가 독립적으로 있어야함
bfs가 visited를 체크하는데, 만약 방문하지 않은 구석이 있다면 bfs는 두번이상 돌것
그 횟수를 리턴받아서 분리되었는지 판단함
"""

def bfs(arr,i,j):

    q.append((i,j))
    visited[i][j] = 1

    while q:
        x, y = q.popleft()
        for di, dj in [[0,1],[0,-1],[-1,0],[1,0]]:
            ni = x + di
            nj = y + dj
            # 범위 밖 넘기기
            if ni < 0 or nj < 0 or nj >= M or ni >= N:
                continue
            # 방문안한 얼음이면 방문표시 후 큐에 넣기
            if arr[ni][nj] != 0 and visited[ni][nj] == 0:
                visited[ni][nj] = 1
                q.append((ni,nj))
            # 얼음 아니면 빈칸 += 1
            elif arr[ni][nj] == 0:
                cnt[x][y] += 1
    return 1

N, M = map(int,stdin.readline().split())
north = [list(map(int,stdin.readline().split())) for _ in range(N)]
q = deque()

is_split = False
day = 0
while 1:
    split = 0
    visited = [[0]*M for _ in range(N)]
    cnt = [[0] * M for _ in range(N)]

    for i in range(N):
        for j in range(M):
            # 들리지 않은 빙산일때 bfs
            if north[i][j] != 0 and visited[i][j] == 0:
                # 이어져있다면 한번만 동작해서 1,
                # 안이어져있다면 2 이상
                split += bfs(north, i,j)
                # print(split)
    # 얼음 깎기
    # -> 바로 안깎는 이유 다음 얼음에 영향미칠까봐
    for i in range(N):
        for j in range(M):
            north[i][j] = max(0,north[i][j] - cnt[i][j])


    # 빙산이 분리됨
    if split >= 2:
        is_split = True
        break
    # 얼음이 남지 않음
    elif split == 0:
        break
    day += 1

if is_split:
    print(day)
else:
    print(0)




