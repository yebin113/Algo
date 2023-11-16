import sys

sys.stdin = open("input.txt")


def bric(i, j):
    # 시작점
    visited[i][j] += arr[i][j]
    # 벽돌에 적힌 숫자 -1 만큼
    for k in range(1, arr[i][j]):
        for di, dj in [[0, 1], [1, 0], [-1, 0], [0, -1]]:
            ni = i + di
            nj = j + dj
            # 벽세우기
            if 0 <= ni < H and 0 <= nj < W:
                # 방문한 곳에 현재 벽돌을 누적..
                visited[ni][nj] += arr[ni][nj]
                # 만약 벽돌이 1보다 크면
                if arr[ni][nj] > 1:
                    # 재귀
                    bric(ni, nj)

    return

import copy

T = int(input())

for tc in range(1, T + 1):
    N, W, H = map(int, input().split())
    arr = [list(map(int, input().split())) for i in range(H)]
    new_arr = copy.deepcopy(arr)
    min_arr = [[9] * W for k in range(H)]
    # N번 수행..
    for i in range(N):
        # 0번부터 W-1칸까지 완전 탐색
        for j in range(W):
            # visited 생성(한번 떨어뜨릴대 깨질 벽돌 범위와 수 누적...)
            visited = [[0] * W for k in range(H)]
            if arr[0][j] == 0:
                continue
            # 시작 위치 주기..
            sti = W-1
            for k in range(W-1,-1,-1):
                if arr[k][j] != 0:
                    sti = k
                    break

            bric(sti, j)
            # 빼주기..
            for k in range(H):
                for m in range(W):
                    new_arr[k][m] = min_arr[k][m] - visited[k][m]
                    # 음수면 0
                    if new_arr[k][m] < 0:
                        new_arr[k][m] = 0
            if sum(sum(min_arr,[])) > sum(sum(new_arr,[])):
                min_arr = copy.deepcopy(new_arr)


    print(f'#{tc} {sum(sum(min_arr,[]))}')
