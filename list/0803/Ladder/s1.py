import sys

sys.stdin = open("input.txt")

T = 10

for tc in range(1, T + 1):
    N = int(input())  # 테스트 케이스 번호
    arr = [list(map(int, input().split())) for _ in range(100)]  # 사다리 배열 받기
    arr_zero = [[0] * 100 for i in range(100)]  # 간 위치를 기록할 것..
    # 마지막 출구 찾기
    for j in range(100):

        if arr[99][j] == 2:
            X_out = j

    i = 98  # 마지막열 부터 거슬러 올라갈거임
    j = X_out
    while i > 0:

        if 0 < j < 99:  # j가 중간일때
            # 왼쪽이 벽안에 있으며, 1이고, 간 위치가 아닐때
            if 0 <= j - 1 <= 99 and arr[i][j - 1] and arr_zero[i][j - 1] == 0:
                # print(f'현재 위치 {i}번째 {j}번 칸 -> 왼쪽으로 이동')
                j = j - 1  # 왼쪽으로 이동
                arr_zero[i][j] = 1  # 지나온 위치임을 표기

            # 오른쪽이 벽안에 있으며, 1이고, 간 위치가 아닐때
            elif 0 <= j + 1 <= 99 and arr[i][j + 1] and arr_zero[i][j + 1] == 0:
                # print(f'현재 위치 {i}번째 {j}번 칸 -> 오른쪽으로 이동')
                j = j + 1  # 왼쪽으로 이동
                arr_zero[i][j] = 1  # 갔다고 표기

            # 오른쪽 왼쪽이 모두 1이 아니고, 위가 간 위치가 아닐때
            elif (arr[i][j + 1] == 0 or arr[i][j - 1] == 0) and arr_zero[i - 1][j] == 0:
                # print(f'현재 위치 {i}번째 {j}번 칸 -> 위로 이동')
                i = i - 1
                arr_zero[i][j] = 1

        else:       # j가 0아니면 99일때
            if j == 0:  # j가 0일땐 오른쪽으로 가던가
                if arr[i][j + 1] and 0 <= j + 1 <= 100 and arr_zero[i][j + 1] == 0:
                    # print(f'현재 위치 {i}번째 {j}번 칸 -> 오른쪽으로 이동')
                    j = j + 1  # 오른쪽으로 이동
                    arr_zero[i][j] = 1
                else:
                    # print(f'현재 위치 {i}번째 {j}번 칸 -> 위로 이동')
                    i = i - 1  # 위로감
                    arr_zero[i][j] = 1
            elif j == 99:   # j가 99일땐 왼쪽으로 가던가
                if arr[i][j - 1] and 0 <= j + 1 <= 100 and arr_zero[i][j - 1] == 0:
                    # print(f'현재 위치 {i}번째 {j}번 칸 -> 왼쪽으로 이동')
                    j = j - 1  # 왼쪽으로 이동
                    arr_zero[i][j] = 1
                else:
                    # print(f'현재 위치 {i}번째 {j}번 칸 -> 위로 이동')
                    i = i - 1       # 위로감
                    arr_zero[i][j] = 1

    print(f'#{tc}', j)
