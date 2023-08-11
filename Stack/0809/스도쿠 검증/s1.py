import sys

sys.stdin = open("input.txt")

T = int(input())

for tc in range(1, T + 1):

    arr = [list(map(int, input().split())) for i in range(9)]
    ans = 1

    # 한줄검증
    for i in range(9):
        # 가로 세로 카운트 정렬
        count_row = [0] * 10
        count_col = [0] * 10
        for j in range(9):
            # i와 j의 위치 바꾸면 행우선, 열우선 한번에 가능
            count_row[arr[i][j]] += 1
            count_col[arr[j][i]] += 1
        for k in range(1, 10):
            # 둘의 카운트 정렬을 확인
            # 각 숫자의 개수가 1개가 아니면 잘못된 스도쿠
            if count_row[k] != 1 or count_col[k] != 1:
                ans = 0

    # 격자검증
    # 세칸씩 건너뛰기
    for n in range(3):
        count_box = [0] * 10
        # 세칸씩 건너 뛰면서 세개의 행 검사
        for i in range(3 * n, 3 * n + 3):
            # 세칸씩 건너뛰면서 세개의 열검사
            for j in range(3 * n, 3 * n + 3):
                # 카운트 정렬
                count_box[arr[i][j]] += 1
        # 카운트 리스트 순회하면서 검증
        for k in range(1, 10):
            if count_box[k] != 1:
                ans = 0

    print(f'#{tc} {ans}')
