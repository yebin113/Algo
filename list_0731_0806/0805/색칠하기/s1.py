import sys
sys.stdin = open("input.txt")

T = int(input())

for tc in range(1, T + 1):
    # 칠한 횟수
    N = int(input())
    # 칠할 영역 초기화
    arr_color = [[0] * 10 for i in range(10)]
    # 칠할 데이터 입력 받기
    for n in range(N):
        # 왼쪽 위 모서리 인덱스 좌표, 오른쪽 아래 모서리 좌표와 색상 정보 color
        arr = list(map(int, input().split()))
        # 주어진 영역에 색상 부여
        for i in range(arr[0], arr[2] + 1):
            for j in range(arr[1], arr[3] + 1):
                arr_color[i][j] += arr[-1]

    # 보라색 색상 세기
    purple  = 0
    # arr_color을 돌면서
    for i in range(10):
        for j in range(10):
            # 해당 색이 3일때 보라색 += 4866괄호검사
            if arr_color[i][j] >= 3:
                purple += 1

    print(f'#{tc} {purple}')
