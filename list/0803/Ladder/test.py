import sys

sys.stdin = open("input.txt")

T = 1

for tc in range(1, T + 1):
    # N = int(input())  # 테스트 케이스 번호
    arr = [list(map(int, input().split())) for _ in range(10)]  # 사다리 배열 받기
    arr_zero = [[0] * 9 for i in range(10)]  # 간 위치를 기록할 것..
    # 마지막 출구 찾기
    for j in range(9):

        if arr[9][j] == 2:
            X_out = j

    i = 9  # 마지막열 부터 거슬러 올라갈거임
    j = X_out

    for i in range(99,-1,-1):
        # 왼쪽이 1이고, 벽안에 있으며, 간 위치가 아닐때
        if arr[i][j - 1] and 0 <= j - 1 <= 8 and arr_zero[i][j - 1] == 0:
            # print(f'현재 위치 {i}번째 {j}번 칸 -> 왼쪽으로 이동')
            j = j - 1  # 왼쪽으로 이동
            arr_zero[i][j] = 1  # 지나온 위치임을 표기
            continue

        # 오른쪽이 1이고, 벽안에 있으며, 간 위치가 아닐때
        elif arr[i][j + 1] and 0 <= j + 1 <= 8 and arr_zero[i][j + 1] == 0:
            # print(f'현재 위치 {i}번째 {j}번 칸 -> 오른쪽으로 이동')
            j = j + 1  # 왼쪽으로 이동
            arr_zero[i][j] = 1  # 갔다고 표기
            continue

        # 오른쪽 왼쪽이 모두 1이 아니고, j 가 벽안에 있으며, 위가 간 위치가 아닐때
        elif arr[i][j + 1] & arr[i][j - 1] == 0 and 0 <= j <= 8 and arr_zero[i - 1][j] == 0:
            # print(f'현재 위치 {i}번째 {j}번 칸 -> 위로 이동')
            pass

        else:
            print(f'현재위치: ({i},{j}) 길잃었다..')
    print(j)
