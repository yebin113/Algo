import sys

sys.stdin = open("input.txt")

# 우 하 좌 상
di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]
T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    arr_zero = [[0] * N for i in range(N)]
    count_num = 1
    dir = 0  # 방향을 지정
    # 시작 위치
    i = 0
    j = 0
    # 시작 위치에 1 지정
    arr_zero[0][0] = 1
    # 총 수를 넣을 횟수-> i는 넣을 수이기도 함

    while count_num < N ** 2:
        # 가야할 방향 제시
        ni = i + di[dir]
        nj = j + dj[dir]
        if 0 <= ni < N and 0 <= nj < N and arr_zero[ni][nj] == 0:
            # 1씩 늘려서 저장
            count_num += 1
            # 이동한 위치에 움직인 거리 할당
            arr_zero[ni][nj] = count_num
            # 위치 갱신
            i = ni
            j = nj
        else:
            # 더 움직일수 없다면 방향 바꿈
            dir += 1
            # 방향이 3보다 크다면 0으로 다시 돌아감(원소가 4개니깐
            if dir > 3:
                dir = 0
    print(f'#{tc}')
    for arr in arr_zero:
        print(*arr)
