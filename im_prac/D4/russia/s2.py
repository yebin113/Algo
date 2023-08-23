import sys

sys.stdin = open("input.txt")

T = int(input())

for tc in range(1, T + 1):
    N, M = map(int, input().split())
    arr = [list(input()) for i in range(N)]
    visited = [0] * N

    # 각행의 흰파빨 개수
    total_list = []
    for i in range(N):
        count_w  = 0
        count_b  = 0
        count_r  = 0
        for j in range(M):
            if arr[i][j] == 'W':
                count_w += 1
            elif arr[i][j] == 'B':
                count_b += 1
            else:
                count_r += 1
        total_list.append([count_w,count_b,count_r])

    # N-2번까지 증가하는 i -> white는 0~i까지
    # i+1 부터 N-1번까지 증가하는 k ->  blue는 i+1부터 k까지
    # k ~ N 까지 증가하는 j   -> red는 k+1 부터 j까지의 합
    min_paint = 1000000
    for i in range(0,N-2):
        for j in range(i+1,N-1):
            paint = 0
            for s in range(0,i+1):
                # W로 칠하기
                paint += total_list[s][1] + total_list[s][2]
            for s in range(i+1,j+1):
                # B로 칠하기
                paint += total_list[s][0] + total_list[s][2]
            for s in range(j+1,N):
                # R로 칠하기
                paint += total_list[s][0] + total_list[s][1]
            if min_paint > paint:
                min_paint = paint
    print(f'#{tc} {min_paint}')
