import sys
sys.stdin = open("input.txt")

T = int(input())
# DFS
def dfs(i,j,chance):
    global max_route
    max_route = max(max_route,visited[i][j])
    for di, dj in [[-1, 0], [0, -1], [1, 0], [0, 1]]:
        ni = i + di
        nj = j + dj
        # 범위 밖이거나 방문했으면 넘기기
        if ni < 0 or ni >= N or nj < 0 or nj >= N or visited[ni][nj] != 0:
            continue
        # 다음이 작으면
        if arr[ni][nj] < arr[i][j]:
            # 방문표시하고
            visited[ni][nj] = visited[i][j] + 1
            # 재귀
            dfs(ni,nj,chance)
            visited[ni][nj] = 0
        # 깎을 기회가 한번 남아있고, 깎으면 등산로 만들기 가능할 때
        elif chance == 1 and arr[ni][nj] - K < arr[i][j]:
            height = arr[ni][nj]
            # 이전 칸보다 1칸만 작아도됨
            arr[ni][nj] = arr[i][j]-1
            # 방문표시하고
            visited[ni][nj] = visited[i][j] + 1
            # 재귀
            dfs(ni, nj, chance-1)
            # 방문표시 돌려놓기
            visited[ni][nj] = 0
            # 깎은거 돌려놓기
            arr[ni][nj] = height




for tc in range(1, T+1):
    N, K = map(int,input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    # 가장 긴 루트
    max_route = 0
    bong = 0
    # 가장 높은 봉우리 높이 찾기
    for i in range(N):
        for j in range(N):
            if bong < arr[i][j]:
                bong = arr[i][j]

    visited=[[0]*N for _ in range(N)]
    # 봉우리 높이인곳에서 dfs 수행
    for i in range(N):
        for j in range(N):
            if arr[i][j] == bong:
                # 방문 표시
                visited[i][j] = 1
                dfs(i,j,1)
                visited[i][j] = 0


    print(f'#{tc} {max_route}')