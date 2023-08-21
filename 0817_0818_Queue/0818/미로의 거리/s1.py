import sys
sys.stdin = open("input.txt")

di = [0,0,-1,1]
dj = [-1,1,0,0]

def bfs(start_i,start_j):
    visited = [[0]*N for i in range(N)]     # 방문 배열을 만든다
    q = [(start_i,start_j)]                 # 큐를 만들어서 시작점을 넣는다
    visited[start_i][start_j] = 1            # 시작점 방문표시
    while q:                # 큐가 빌때까지
        i, j = q.pop(0)      # 큐를 팝한다
        for k in range(4):      # 주변 인덱스를 탐방
            # 새로운 위치
            ni = i + di[k]
            nj = j + dj[k]
            # 새로운 위치가 범위 안에 있고, 벽이 아니며 방문한 곳이 아닐때
            if 0<=ni<N and 0<=nj<N and arr[ni][nj] != 1 and visited[ni][nj] == 0:
                q.append((ni,nj))   # 큐에 좌표 추가
                visited[ni][nj] = visited[i][j] + 1     # 방문표시는 이전 위치의 값 + 1로

                if arr[ni][nj] == 3:        # 탈출로일때
                    return visited[ni][nj] - 2
    return 0



def find_start(arr):
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 2:
                return i,j


T = int(input())

for tc in range(1, T+1):
    N = int(input())
    # N * N 배열의 미로
    arr = [list(map(int, input())) for _ in range(N)]
    start_i,start_j = find_start(arr)       # 시작점 찾기



    print(f'#{tc} {bfs(start_i,start_j)}')