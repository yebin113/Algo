import sys
input = sys.stdin.readline


def bfs(sti, stj):
    global visited
    if 0<=sti+1<n and 0<=stj+1<m:
        visited[sti][stj+1] = 1
        visited[sti+1][stj] = 1
    else:
        return 1
    # 오른쪽과 아래, 오른쪽 아래 세 방향 탐색해보기
    if arr[sti][stj+1] == 1 and arr[sti+1][stj] == 1 and arr[sti+1][stj+1] == 1:
        visited[sti + 1][stj+1] = 1
        # print(arr[sti][stj+1],arr[sti+1][stj],arr[sti+1][stj+1])
    else:
        return 1
    # 시작 길이 2
    length = 2
    x = sti + 1
    y = stj + 1
    # print(f'sti {sti} stj {stj}')
    while True:
        check = False
        # 대각선 방향
        x += 1
        y += 1
        for k in range(1, length+1):
            # for l in range(n):
            #     print(visited[l])
            # print()
            nx = x - k
            ny = y - k
            # print(f'nx {nx} ny {ny} arr[nx][ny] {arr[nx][ny]}')
            if 0 <= nx < n and 0 <= ny < m and arr[nx][y] == 1 and arr[x][ny] == 1:
                visited[nx][ny] = 1
                continue
            else:
                check = True
                break
        if check:
            break
        length += 1

    return length * length







dxy_plus = [[0, 1], [1, 0],[1,1]]
dxy_two = [[0, 1], [1, 0]]
n, m = map(int, input().split())
arr = [list(map(int, input().strip())) for _ in range(n)]

visited = [[0] * m for _ in range(n)]
max_area = 0
for i in range(n):
    for j in range(m):
        if arr[i][j] == 1 and visited[i][j] == 0:
            visited[i][j] = 1
            max_area = max(max_area,bfs(i, j))

print(max_area)