import sys

sys.stdin = open("input.txt")

T = int(input())

for tc in range(1, T + 1):
    # 스도쿠 입력
    arr = [list(map(int, input().split())) for _ in range(9)]
    ans = 1
    for i in range(9):
        # 가로 세로 한줄의 갯수를 셀 리스트
        count_row = [0] * 10
        count_col = [0] * 10

        for j in range(9):
            # 가로 세로 요소 카운팅 정렬
            count_row[arr[i][j]] += 1
            count_col[arr[j][i]] += 1
            # print(arr[i][j],count_row,arr[j][i],count_col)

        for k in range(1, 10):
            # print(count_row,count_col)
            # 카운팅 정렬한 요소가 1개가 아니라면 올바르지 않은 스도쿠
            if count_row[k] != 1 or count_col[k] != 1:
                ans = 0
            else:
                ans = 1

    for i in range(3):
        for j in range(3*i, 3*i+3):
            count_three = [0] * 10
            for m in range(3 * i, 3 * i + 3):
                count_three[arr[i][m]] += 1

            print(count_three)

        for k in range(1, 10):
            # 카운팅 정렬한 요소가 1개가 아니라면 올바르지 않은 스도쿠
            if count_three[k] != 1:
                ans = 0

    # print(f'#{tc} {ans}')
