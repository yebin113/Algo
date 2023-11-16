def bfs():
    visited = [[T+100]*M for _ in range(N)]
    visited[0][0] = 0
    q = [(0,0)]
    # 검 발견 전 변수 최댓값으로 설정해두기
    find_grim = T+100
    while q:
        i,j = q.pop(0)
        # 도착했다면 검을 찾았을 때랑 현재랑 비교해서 작은값으로 리턴
        if i==N-1 and j == M-1:
            return min(find_grim,visited[i][j])
        for di,dj in [[0,1],[1,0],[-1,0],[0,-1]]:
            ni = di + i
            nj = dj + j
            # 델타 탐색, 범위 밖이거나 벽일때 넘기기
            if ni < 0 or ni >= N or nj < 0 or nj>=M or arr[ni][nj]== 1:
                continue
            # 더 긴 루트로 왔다면 넘기기
            if visited[ni][nj] <= visited[i][j]+1:
                continue
            # 방문표시
            visited[ni][nj]=visited[i][j]+1
            q.append((ni,nj))
            # 검을 발견했다면
            if arr[ni][nj] == 2:
                find_grim = visited[ni][nj] + N-1 - ni + M-1 - nj
                # 도착지가 벽이라면 무조건 그림을 챙겨가야 함
                if arr[-1][-1] == 1:
                    return find_grim
    if find_grim <= T:
        return find_grim
    else:
        # q가 도착지에 도달하지 못하면 실패해야하기때문에 return을 충분히 큰값으로 줌
        return T+100




N,M,T = map(int,input().split())
arr = [list(map(int,input().split())) for _ in range(N)]

# 가로 세로 더한 값보다 시간이짧으면 어차피 실패
if T < N+M-2:
    print('Fail')

else:
    # 공주에게 갈 수 있는 최단 시간
    time = bfs()
    # 시간이 넘지않을때
    if time <= T:
        print(time)
    else:
        print('Fail')


