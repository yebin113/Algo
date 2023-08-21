import sys
sys.stdin = open("input.txt")

di = [0,0,-1,1]
dj = [-1,1,0,0]

T = 10


def bfs():
    visited = [[0] * 100 for i in range(100)]  # 방문리스트
    visited[1][1] = 1  # 시작점 표기
    q = [(1, 1)]  # 큐 생성
    while q:  # 큐가 존재할때까지
        i, j = q.pop(0)  # 팝
        for k in range(4):
            ni = i + di[k]
            nj = j + dj[k]      # 새로 갈 위치
            # 새로운 위치가 범위 안에 있고 벽이 아니며 방문된 곳이 아닐때
            if 0<=ni<100 and 0<=nj<100 and arr[ni][nj] != 1 and visited[ni][nj] ==0:
                # 방문 표시
                visited[ni][nj] = visited[i][j] + 1
                # 큐에 좌표 넣기
                q.append((ni,nj))
            if arr[ni][nj] == 3:
                return 1
    return 0

for _ in range(1, T + 1):
    tc = int(input())
    arr = [list(map(int, input())) for i in range(100)]

    print(f'#{tc} {bfs()}')
