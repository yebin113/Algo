import sys

sys.stdin = open("input.txt")

T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for i in range(N)]

    print(f'#{tc}')

    # 인덱스 범위 그려보면서 풀면 됨
    for i in range(N):
        for j in range(N):
            print(arr[N - 1 - j][i], end='')
        print(" ", end='')
        for j in range(N):
            print(arr[N - 1 - i][N-1-j], end='')
        print(" ", end='')
        for j in range(N):
            print(arr[j][N-1-i], end='')
        print()
