import sys
sys.stdin = open("input.txt")

T = int(input())

def bfs(i,j):
    visited = [[int(1e9)]*N for i in range(N)]
    visited[i][j] = 1
    q = [(i,j)]
    while q:
        i,j = q.pop(0)
        for di,dj in dxy:
            ni = i + di
            nj = j + dj
            # 범위를 벗어나면 넘기기
            if ni < 0 or ni >= N or nj < 0 or nj >= N:
                continue
            # 큐에 넣기
            q.append((ni,nj))
            # 최소로 갱신

            visited[ni][nj] = min(visited[i][j] + arr[ni][nj],visited[ni][nj])




    return visited[-1][-1] - 1


dxy = [[0,1],[1,0]]
for tc in range(1, T+1):
    # 지도의 크기
    N = int(input())
    # 지도
    arr = [list(map(int, input())) for _ in range(N)]
    ans = bfs(0,0)
    print(f'#{tc} {ans}')