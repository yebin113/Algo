import sys

sys.stdin = open("input.txt")

T = int(input())


def dfs(y, x, number):
    # 기저조건
    if len(number) == 7:
        result.add(number)
        return
    for di, dj in [[0, 1], [-1, 0], [1, 0], [0, -1]]:
        ny = y + di
        nx = x + dj
        # 갈 수 없는 위치면 continue
        if ny < 0 or ny >= 4 or nx < 0 or nx >= 4:
            continue
        # 갈 수 있다면 다음 위치로
        dfs(ny,nx,number + arr[ny][nx])


for tc in range(1, T + 1):
    arr = [input().split() for i in range(4)]
    result = set()
    for i in range(4):
        for j in range(4):
            dfs(i, j, arr[i][j])
    print(f'#{tc} {len(result)}')
