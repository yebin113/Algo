import sys

sys.stdin = open("input.txt")

T = int(input())

for tc in range(1, T + 1):
    # 배열의 크기 N * N , 파리채의 크기 M * M
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    # 최대로 죽은 범위의 파리가 저장될 변수
    max_killed_fly = 0

    for i in range(N - M+1):      # arr[i][j]의 범위가 0 ~ N-M
        for j in range(N - M+1):
            killed_fly = 0      # 각 요소 마다 초기화 시켜줌
            for l in range(i, i + M):   # a[i][j]를 시작점으로 M만큼의 가로
                for m in range(j, j + M):   # a[i][j]를 시작점으로 M만큼의 세로
                    killed_fly += arr[l][m]  # 범위내(파리채 범위내) 모든 파리 수를 누적

            if max_killed_fly < killed_fly:  # 현재 잡은 파리수가 최댓값이라면
                max_killed_fly = killed_fly     # 저장

    print(f'#{tc} {max_killed_fly}')
