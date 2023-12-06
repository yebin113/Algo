from collections import deque
def bfs(i,j,k):
    global min_minutes
    q = deque([(i,j,k)])
    visited = [[[0]*C for _ in range(R)] for _ in range(L)]
    visited[i][j][k] = 1

    while q:
        i,j,k = q.popleft()

        for di , dj, dk in dir:
            ni = i + di
            nj = j + dj
            nk = k + dk
            if 0<=ni<L and 0<=nj<R and 0<=nk<C and visited[ni][nj][nk] ==0 and building[ni][nj][nk] != '#':

                q.append((ni,nj,nk))
                visited[ni][nj][nk] = visited[i][j][k] + 1
                # 도착한다면
                if building[ni][nj][nk] == 'E':
                    # 최소 갱신
                    min_minutes = min(min_minutes,visited[ni][nj][nk]-1)



dir = [[0,0,1],[0,0,-1],[0,-1,0],[0,1,0],[1,0,0],[-1,0,0]]
# L(1 ≤ L ≤ 30)은 상범 빌딩의 층 수
# R(1 ≤ R ≤ 30)과 C(1 ≤ C ≤ 30)는 한 층의 행과 열의 개수
while 1:
    L,R,C = map(int,input().split())
    if L == 0 and R == 0 and C == 0:
        break
    building = []
    min_minutes = 100000000000000000000000000000000
    start = [0,0,0]
    start_check = False
    for i in range(L):
        floor = [list(map(str,input())) for _ in range(R)]
        blank = input()
        # 시작점 저장
        for j in range(R):
            for k in range(C):
                if floor[j][k] == "S":
                    start = [i,j,k]
                    start_check = True
                    break
            if start_check:
                break

        building.append(floor)

    bfs(*start)
    if min_minutes < 100000000000000000000000000000000:

        print(f"Escaped in {min_minutes} minute(s).")
    else:
        print('Trapped!')

