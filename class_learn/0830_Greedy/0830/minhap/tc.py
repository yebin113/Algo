import sys
sys.stdin = open("input.txt")
T = int(input())
for tc in range(1, T+1):
    # N * N 배열
    N = int(input())
    arr = [list(map(int, input().split())) for i in range(N)]

    # 2중반복
    for i in range(N):
        for j in range(N):
            if i == j == 0:
                continue
            # 1. 첫번째 행에서 우측
            if i == 0:
                arr[i][j] += arr[i][j-1]    # 이동하면서 값 증가시키기
            # 2. 첫번째 열에서 아래
            if j == 0:
                arr[i][j] += arr[i-1][j]    # 이동하면서 값 증가시키기
            # 3. 나머지 모든 경우 greedy -> 우측과 아래쪽 중 값이 작은 방향으로
            else:
                arr[i][j] += min(arr[i][j-1],arr[i-1][j])
    print(arr[N-1][N-1])