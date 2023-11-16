def dfs(x, y, dir, dot):
    global check
    if dir == 3 and x == i and y == j:
        check = True
        return
    # 다음
    nx1 = x + dxy[dir][0]
    ny1 = y + dxy[dir][1]

    if 0 <= nx1 < N and 0 <= ny1 < M and arr[x][y] == dot:
        dfs(nx1,ny1,dir,dot)
    if dir < 3:
        nx2 = x + dxy[dir+1][0]
        ny2 = y + dxy[dir+1][1]

        if 0 <= nx2 < N and 0 <= ny2 < M and arr[x][y] == dot:
            dfs(nx2, ny2, dir+1, dot)



dxy = [[0,1], [1,0], [0,-1], [-1, 0]]
N, M = map(int, input().split())
arr = [list(input()) for _ in range(N)]
check = False
for i in range(N):
    for j in range(M):
        dfs(i,j,0,arr[i][j])
        if check:
            print('Yes')
            break
    if check:
        break

else:
    print('No')