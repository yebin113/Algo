import sys
sys.stdin = open("input.txt")

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    colored = [[0]*10 for i in range(10)]
    for m in range(N):
        arr = list(map(int, input().split()))
        # 열 인덱스 범위만큼
        for i in range(arr[0], arr[2] + 1):
            # 행 인덱스 범위만큼
            for j in range(arr[1], arr[3] + 1):
                colored[i][j] += arr[4]
    purple = 0
    # 3이상이면 보라색
    for i in range(10):
        for j in range(10):
            if colored[i][j] >= 3:
                purple += 1
    print(f'#{tc} {purple}')

