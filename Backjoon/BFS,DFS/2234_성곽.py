"""
각 숫자에 따라 갈수있는 방향을 딕셔너리에 저장
모든 위치를 돌며 bfs로 영역을 탐색한다. 이미 다른 영역인 곳은 탐색 X
bfs를 돌때 영역은 area라는 리스트에 좌표를 모두 저장
q를 다 돌았다면 영역의 크기로 가장 큰 영역의 크기를 갱신해주고, 영역 개수(cnt) + 1 해줌
해당 영역의 크기(len(area)와 영역 번호(cnt)를 visited에 저장한다
모든 bfs가 종료되면 이중 반복문을 돌면서 상하좌우의 인접한 방이 같은 방이 아닐때,
(visited[i][j][1]가 같다면 같은 영역이니 패스) 영역크기의 합(max_remove_area)을 큰값으로 갱신해줌
"""

from collections import deque
nsdw = {
    '동':[0,1],
    '서':[0,-1],
    '남':[1,0],
    '북':[-1,0]
}
dir = {
    # 벽이 없다
    0: [nsdw['동'],nsdw['서'],nsdw['남'],nsdw['북']],
    # 서쪽에만 벽이있다
    1: [nsdw['동'],nsdw['남'],nsdw['북']],
    # 북쪽에만 벽이있다
    2: [nsdw['동'],nsdw['서'],nsdw['남']],
    # 동쪽에만 벽이있다
    4: [nsdw['서'],nsdw['남'],nsdw['북']],
    # 남쪽에만 벽이 있다
    8: [[0, 1], [0, -1], [-1, 0]],
    # 서북에 벽이 있다
    3: [nsdw['동'],nsdw['남']],
    # 서동
    5: [nsdw['남'],nsdw['북']],
    # 서남
    9: [nsdw['동'],nsdw['북']],
    # 북동
    6: [nsdw['서'],nsdw['남']],
    # 북남
    10: [nsdw['동'],nsdw['서']],
    # 동남
    12: [nsdw['서'],nsdw['북']],
    # 동만 벽이 없음
    11: [nsdw['동']],
    # 서만 벽이 없음
    14: [nsdw['서']],
    # 남만 벽이 없음
    7: [nsdw['남']],
    # 북만 벽이 없음
    13: [nsdw['북']],
    # 사방
    15: []
}


def bfs(i, j):
    global max_area,cnt
    q = deque()
    q.append((i, j))
    area = [(i,j)]
    while q:
        i, j = q.popleft()
        for di, dj in dir[arr[i][j]]:
            ni = i + di
            nj = j + dj
            if not (0 <= ni < M and 0 <= nj < N) or (ni, nj) in area or visited[ni][nj] != 0:
                continue
            q.append((ni, nj))
            area.append((ni, nj))
    area_cnt = len(area)
    max_area = max(max_area,area_cnt)
    cnt += 1
    for si, sj in area:
        visited[si][sj] = [area_cnt,cnt]



N, M = map(int, input().split())
arr = []
for _ in range(M):
    arr.append(list(map(int, input().split())))
visited = [[0] * N for _ in range(M)]
cnt = 0
max_area = 0
max_remove_area = 0
for i in range(M):
    for j in range(N):
        if visited[i][j] != 0:
            continue
        bfs(i,j)
for i in range(M):
    for j in range(N):
        for di, dj in dir[0]:
            ni = i + di
            nj = j + dj
            if not(0<=ni<M and 0<=nj<N) or visited[i][j][1] == visited[ni][nj][1]:
                continue
            max_remove_area = max(max_remove_area,visited[i][j][0]+visited[ni][nj][0])
print(cnt)
print(max_area)
print(max_remove_area)
