import sys
sys.stdin = open("input.txt")

T = 10



for _ in range(1, T+1):
    tc = int(input())
    arr = [list(map(int, input().split())) for i in range(100)]
    visited = [[0]*100 for i in range(100)]
    X_out = 0
    # 출구찾기
    for i in range(100):
        if arr[99][i] == 2:
            X_out = i

    i = 98
    j = X_out
    while i != 0:
        # 왼쪽이 존재하고, 왼쪽이 1이며, 방문하지 않았을때
        while 0 <= j-1 < 100 and arr[i][j-1] == 1 and visited[i][j-1] == 0:
            j -= 1
            visited[i][j] = 1
        # 오른쪽이 존재하고 오른쪽이 1이며 방문하지 않았을때
        while 0 <= j + 1 < 100 and arr[i][j + 1] == 1 and visited[i][j + 1] == 0:
            j += 1
            # 방문표시
            visited[i][j] = 1
        # 위로 이동
        i -= 1

    # 반복이 끝났을때의 j 위치를 출력합니다
    print(f'#{tc} {j}')