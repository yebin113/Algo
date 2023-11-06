def dfs(x,y,dot,cnt):
    global check

    if check:
        return
    for k in range(4):
        ni = x + dxy[k][0]
        nj = y + dxy[k][1]
        # 4개의 점 이상이 연결되고 현재의 위치로 돌아왔을때
        if ni == i and nj == j and cnt >= 4:
            check = True
            # print('완성')
            return

        # 범위에서 벗어나거나, 들렀던 곳이거나 같은 색이 아닐때 넘기기
        if ni < 0 or nj < 0 or ni >= N or nj >= M or visited[ni][nj] != 0 or arr[ni][nj] != dot:
            # print(f'다음 위치 {ni} {nj}')
            # try:
            #     print(f'원래 색 {dot} 다음 색 {arr[ni][nj]}')
            # except:
            #     pass
            continue


        visited[ni][nj] = 1
        # print(f'지금 방문 현환')
        # for h in range(N):
        #     print(visited[h])
        dfs(ni,nj,dot,cnt + 1)
        visited[ni][nj] = 0



dxy = [[0, 1], [1, 0], [0, -1], [-1, 0]]
N, M = map(int, input().split())
arr = [list(input()) for _ in range(N)]
check = False
visited = [[0]*M for _ in range(N)]
for i in range(N):
    for j in range(M):
        if visited[i][j]== 0:
            visited[i][j] = 1
            dfs(i,j,arr[i][j],1)

        if check:
            print('Yes')
            break
    if check:
        break

else:
    print('No')