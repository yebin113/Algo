import sys

sys.stdin = open("input.txt")

T = int(input())

for tc in range(1, T + 1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for i in range(N)]
    max_sum_plus = 0

    di = [0, 0, -1, 1]
    dj = [1, -1, 0, 0]

    for i in range(N):
        for j in range(M):
            sum_plus = arr[i][j]    # 현재위치부터 더함
            for k in range(1,arr[i][j]+1):  # 현재위치의 크기만큼 주변인덱스를 더할것
                for m in range(4):
                    ni = i + k * di[m]      # 인덱스 재 정의
                    nj = j + k * dj[m]      # 이전에는 1만큼 갔다면 현재는 k만큼 더 가야함 반복을 하기 위해 곱해줌
                    if 0 <= ni < N and 0 <= nj < M:     # 벽세우기
                        sum_plus += arr[ni][nj]     # 합 구하기
            if max_sum_plus < sum_plus:     # 합중의 최댓값 구하기
                max_sum_plus = sum_plus

    print(f'#{tc} {max_sum_plus}')
