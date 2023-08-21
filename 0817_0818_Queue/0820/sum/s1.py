import sys
sys.stdin = open("input.txt")

T = 10

for _ in range(1, T+1):
    tc = int(input())
    arr = [list(map(int,input().split())) for i in range(100)]
    sum_max = 0
    # 가로 세로줄 합 구하기
    for i in range(100):
        # 매 열과 행마다 초기화
        sum_row = 0
        sum_col = 0
        # 각 열과 행의 합을 누적
        for j in range(100):
            sum_row += arr[i][j]
            sum_col += arr[j][i]
        # 최댓값 갱신
        if sum_max < sum_row:
            sum_max = sum_row
        if sum_max < sum_col:
            sum_max = sum_col

    # 대각선 의 합 초기화
    sum_d1 = 0
    sum_d2 = 0
    for i in range(100):
        sum_d1 += arr[i][i]
        sum_d2 += arr[i][99-i]
    if sum_max < sum_d1:
        sum_max = sum_d1
    if sum_max < sum_d2:
        sum_max = sum_d2

    print(f'#{tc} {sum_max}')