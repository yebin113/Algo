import sys

sys.stdin = open("input.txt")

T = int(input())

for tc in range(1, T + 1):
    # N x N 배열 안의 숫자는 해당 영역에 존재하는 파리의 개체 수
    # M은 스프레이 세기
    N, M = map(int, input().split())
    # 해당 영역에 존재하는 파리의 개수가 담긴 배열
    arr = [list(map(int, input().split())) for i in range(N)]
    # 십자가 모양
    dx1 = [0, 0, -1, 1]
    dy1 = [-1, 1, 0, 0]
    # x자 모양
    dx2 = [-1, -1, 1, 1]
    dy2 = [-1, 1, -1, 1]

    # 죽인 파리의 최대수
    max_kill_fly = 0
    # 파리수가 담긴 배열을 돌기
    for i in range(N):
        for j in range(N):
            # 중간 지점의 파리 마리수
            kill_fly_plus = arr[i][j]
            kill_fly_X = arr[i][j]

            for m in range(4):  # 네방향 지정해돈 리스트를 순회하며
                for k in range(1,M):  # M번만큼 반복해야함-> 1부터 시작해야홤(스프레이 범위)
                    # 십자가 모양
                    nx = i + dx1[m] * k
                    ny = j + dy1[m] * k
                    # 벽세우기
                    if 0 <= nx < N and 0 <= ny < N:
                        kill_fly_plus += arr[nx][ny]
                        # print(f'중간 {arr[i][j]},더할 수 위치{nx},{ny}, 더할 수 {arr[nx][ny]}, 최종 합 {kill_fly_plus}')
                    # 엑스자 모양
                    nx2 = i + dx2[m] * k
                    ny2 = j + dy2[m] * k
                    # 벽세우기
                    if 0 <= nx2 < N and 0 <= ny2 < N:
                        kill_fly_X += arr[nx2][ny2]
            # 최댓값 갱신
            if max_kill_fly < kill_fly_plus:
                max_kill_fly = kill_fly_plus
            if max_kill_fly < kill_fly_X:
                max_kill_fly = kill_fly_X
    print(f'#{tc} {max_kill_fly}')
