import sys

sys.stdin = open("input.txt")

T = int(input())

for tc in range(1, T + 1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for i in range(N)]
    max_sum_plus = 0

    for i in range(N):
        for j in range(M):
            sum_plus = arr[i][j]  # 터트린 꽃가루 수
            for di, dj in [[0, 1], [1, 0], [0, -1], [-1, 0]]:  # 인접에 대해
                ni, nj = i, j
                for p in range(arr[i][j]):
                    ni, nj = ni + di, nj + dj
                    if 0 <= ni < N and 0 <= nj < M:  # 범위 안에 들때
                        sum_plus += arr[ni][nj]  # 주변칸 풍선의 꽃가루 수

                    else:
                        break
            if max_sum_plus < sum_plus:
                max_sum_plus = sum_plus

    print(f'#{tc} {max_sum_plus}')
