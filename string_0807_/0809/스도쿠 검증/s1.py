import sys

sys.stdin = open("input.txt")

T = int(input())

for tc in range(1, T + 1):

    arr = [list(map(int, input().split())) for i in range(9)]
    ans = 1

    # 한줄검증
    for i in range(9):
        count_row = [0] * 10
        count_col = [0] * 10
        for j in range(9):
            count_row[arr[i][j]] += 1
            count_col[arr[j][i]] += 1
        for k in range(1, 10):
            if count_row[k] != 1 or count_col[k] != 1:
                ans = 0

    # 격자검증
    for n in range(3):
        count_box = [0] * 10
        for i in range(3 * n, 3 * n + 3):
            for j in range(3 * n, 3 * n + 3):
                count_box[arr[i][j]] += 1
        for k in range(1, 10):
            if count_box[k] != 1:
                ans = 0

    print(f'#{tc} {ans}')
