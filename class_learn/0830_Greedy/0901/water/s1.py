import sys
sys.stdin = open("input.txt")

"""
물에서부터 BFS해보기.. ?>
"""
di = [0,0,-1,1]
dj = [-1,1,0,0]
def bfs(i,j):
    # 방문배열 생성
    visited = [[0] * M for _ in range(N)]
    # 큐에 첫 점 넣기
    q = [(i,j)]
    visited[i][j] = 1
    while q:
        # 큐에서 꺼낸다..
        i,j = q.pop(0)
        # 인접한 네 방향
        for k in range(4):
            ni = i + di[k]
            nj = j + dj[k]
            # 인접한 방향이 범위 안에 있고 물이면
            if 0<=ni<N and 0<=nj<M and arr[ni][nj] =='W':
                # 마지막 누적값을 리턴
                return visited[i][j]

            # 인접한 방향이 범위 안에 있고 방문하지 않았으며.. 땅이면
            elif 0<=ni<N and 0<=nj<M and arr[ni][nj] =='L' and visited[ni][nj] == 0:
                # 방문 표에 누적값
                visited[ni][nj] = visited[i][j] + 1
                # 큐에 넣는다
                q.append((ni,nj))



T = int(input())

for tc in range(1, T+1):
    N, M = map(int,input().split())
    arr = [list(input()) for i in range(N)]
    # 총 합
    cnt = 0
    # 각 위치에서
    for i in range(N):
        for j in range(M):
            # 땅일때
            if arr[i][j] != 'W':
                cnt += bfs(i,j)


    print(f'#{tc} {cnt}')