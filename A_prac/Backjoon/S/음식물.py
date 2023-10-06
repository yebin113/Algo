import sys
import pprint
dxy = [[0, -1], [-1, 0], [0, 1], [1, 0]]
# 세로 길이 N과 가로 길이 M 그리고 음식물 쓰레기의 개수 K
N, M, K = map(int, sys.stdin.readline().split())
arr = [[0] * M for _ in range(N)]
# K개의 줄에 음식물이 떨어진 좌표 (r, c)
for _ in range(K):
    r, c = map(int, sys.stdin.readline().split())
    r -= 1
    c -= 1
    counts = 0
    for di, dj in dxy:
        ni = r + di
        nj = c + dj
        # 주변이 범위 안에 있고, 0이 아닐때!
        if 0 <= ni < N and 0 <= nj < M and arr[ni][nj] != 0:
            counts += 1
            arr[r][c] = arr[ni][nj] + counts
            pprint.pp(arr)
        else:
            arr[r][c] = 1
max_size = 0
for i in range(N):
    for j in range(M):
        if arr[i][j] != 0:
            max_size = max(arr[i][j], max_size)

print(max_size)
