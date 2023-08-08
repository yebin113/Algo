import sys

sys.stdin = open("input.txt")

# 숫자는 n제곱까지
# 우 하 좌 상으로 반복
# 벽에 도달하면 turn
# if 상 (idx == 3):

# 우 하 좌 상
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    arr_zero = [[0] * N for i in range(N)]


    count_snail = 1  # 달팽이가 이동하면서 값을 증가시키고 기록할 변수
    x, y = 0, 0  # 시작 좌표 설정
    dir = 0  # 이동할 방향
    arr_zero[x][y] = count_snail    # 시작 위치에 1을 기록

    # 달팽이 반복 시작
    while count_snail < N**2:   # N*N만큼 판이 만들어지니까, 3*3 -> 9
        nx = x+dx[dir]  # nx = 0 + dx[0] -> 0
        ny = y+dy[dir]  # ny = 0 + dy[0] -> 0
        # 다음 조사 위치가 0보다 크거나 같고, N보다 작다면, 그리고 다음 위치가 0이면
        if 0 <= nx < N and 0 <= ny < N and arr_zero[nx][ny] == 0:    # 벽세우기 & 안 간 위치 파악
            count_snail += 1
            arr_zero[nx][ny] = count_snail      # 현재 조사하는 곳에 count 할당
            # 현재 위치 갱신
            x, y = nx, ny

        else:   # 더이상 해당 방향으로 이동할 수 없을때
            dir += 1
            # dir은 4개를 순회해야 하기 때문에 인덱스 초과시 0으로 돌아와야함
            if dir > 3:
                dir = 0

    print(f'#{tc}')
    for i in range(N):
        for j in range(N):
            print(arr_zero[i][j],end=' ')
        print()
