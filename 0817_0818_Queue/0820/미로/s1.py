import sys
sys.stdin = open("input.txt")

T = 10

di = [0,0,-1,1]
dj = [-1,1,0,0]
def bfs(sti,stj):
    visited = [[0]*100 for i in range(100)]
    visited[sti][stj] = 1
    q = [(sti,stj)]


    while q:
        # pop(0) 이거 0 넣는거 자꾸 까먹음
        i,j = q.pop(0)
        for k in range(4):
            ni = i + di[k]
            nj = j + dj[k]
            # 범위 안에 있고 벽이 아니며 방문했던 장소가 아닐때
            if 0<=ni<100 and 0<=nj<100 and maze[ni][nj] != 1 and visited[ni][nj] == 0:
                # q 에 추가
                q.append((ni,nj))
                # 방문표시 & 간 거리
                visited[ni][nj] = visited[i][j] + 1
                # 탈출로 1 리턴
                if maze[ni][nj] == 3:
                    return 1
    # 다 돌고도 탈출로가 없으면 0을 리턴
    return 0



for tc in range(1, T+1):
    n = int(input())
    # 미로
    maze = [list(map(int,input())) for i in range(100)]


    print(f'#{tc} {bfs(1,1)}')