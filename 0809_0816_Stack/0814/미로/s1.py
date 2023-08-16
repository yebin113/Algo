import sys
sys.stdin = open("input.txt")
from pprint import pprint
# 출발은 2, 도착은 3, 통로는 0
# 2에서 출발해서 0인 통로를 따라 이동하면 맨 윗줄의 3에 도착할 수 있는지 확인하면 된다.
T = int(input())

dx = [0,-1,0,1]
dy = [-1,0,1,0]
dir = 0
for tc in range(1, T+1):
    # 미로의 크기
    N = int(input())
    # 미로 배열
    arr = [list(input()) for i in range(N)]
    # 도착할 수 있으면 1, 아니면 0을 출력한다.

    ans = 1
    # 방문리스트
    visited = [[0]*N for i in range(N)]
    stack = []
    for i in range(N):
        for j in range(N):
            if arr[i][j] == '2':
                # 시작 점 저장
                start_idx = (i,j)

    i = start_idx[0]
    j = start_idx[1]
    visited[i][j] = 1
    while arr[i][j] != '3':

        ni = i + dx[dir]
        nj = j + dy[dir]

        # 벽 안에 있고, 방문하지 않았으며, 통로인 0일때
        if 0 <= ni < N and  0 <= nj < N and visited[ni][nj] == 0 and arr[ni][nj] != '1':
            # stack에 쌓음
            stack.append((ni,nj))
            # 방문했다고 표시
            visited[ni][nj] = 1
            # 위치 갱신
            i = ni
            j = nj

            # 벽밖으로 나갔거나 벽을 부딫히거나 방문한 곳일때
        elif ni >= N or nj >= N or arr[ni][nj] == '1' or visited[ni][nj] == 1:
            # 갈림길이 나올때까지 pop
            # 사방을 둘러봤을때 간곳이 아니고, 벽이 아닌곳을 찾을때 까지
            # while 0 <= ni < N and  0 <= nj < N
            i = stack.pop()[0]
            j = stack.pop()[1]
            for k in range(4):
                dir += 1
                if dir == 4:
                    dir = 0
                # 가본곳이 아니고 통로라면
                if arr[ni][nj] == 0 and visited[ni][nj] == 0:
                    break

        print(i,j)


    print(f'#{tc} {ans}')