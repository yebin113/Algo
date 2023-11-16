import sys
sys.stdin = open("input.txt")

T = int(input())

plus = [[0,1],[0,-1],[-1,0],[1,0]]
updown = [[-1,0],[1,0]]
leftright = [[0,1],[0,-1]]
upright = [[-1,0],[0,1]]
downright = [[1,0],[0,1]]
downleft = [[1,0],[0,-1]]
upleft = [[-1,0],[0,-1]]

structure = {
        1:plus,
        2:updown,
        3:leftright,
        4:upright,
        5:downright,
        6:downleft,
        7:upleft
}
structure_help = {
    0:'0',
        1:'╈',
        2:'┃',
        3:'━',
        4:'┗',
        5:'┏',
        6:'┐',
        7:'┛'
}
def bfs(i,j):
    q = [(i,j)]
    visited = [[0]*M for _ in range(N)]
    visited[i][j] = 1
    sec = 0
    flag = True
    while q and visited[i][j] < L:
        sec += 1
        # 큐에서 조사할 인덱스 꺼냄
        i,j = q.pop(0)
        # 그리고 현재 위치
        dij = structure[arr[i][j]]
        for di,dj in dij:
            ni = i + di
            nj = j + dj
            if visited[i][j] == L:
                flag = False
                break
            # 아래로갈땐
            if di == 1:
                # 범위 안에 있고 다음칸이 위로 갈수 있는 구조물일때,, 그리고 방문하지않은 곳이면
                if 0<= ni < N and 0<= nj <M and arr[ni][nj] in [1,2,4,7] and visited[ni][nj] == 0:
                    visited[ni][nj] = visited[i][j]+1
                    q.append((ni,nj))
                    # print(f'고,,지금 {i} {j} 새로운 위치 {ni} {nj} 방향 V 지금 칸 {structure_help[arr[i][j]]} 다음 칸 {structure_help[arr[ni][nj]]}')

            # 위로 갈땐
            elif di == -1:
                # 범위 안에 있고 다음칸이 아래로 갈수 있는 구조물일때,, 그리고 방문하지않은 곳이면
                if 0<= ni < N and 0<= nj <M and arr[ni][nj] in [1,2,5,6] and visited[ni][nj] == 0:

                    visited[ni][nj] = visited[i][j]+1
                    q.append((ni,nj))
                    # print(f'고,,지금 {i} {j} 새로운 위치 {ni} {nj} 방향 ㅅ 지금 칸 {structure_help[arr[i][j]]} 다음 칸 {structure_help[arr[ni][nj]]}')

            elif dj == 1:
                # 범위 안에 있고 다음칸이 오른쪽으로 갈수 있는 구조물일때,, 그리고 방문하지않은 곳이면
                if 0<= ni < N and 0<= nj <M and arr[ni][nj] in [1,3,6,7] and visited[ni][nj] == 0:
                    visited[ni][nj] = visited[i][j]+1
                    q.append((ni,nj))
                    # print(f'고,,지금 {i} {j} 새로운 위치 {ni} {nj} 방향 > 지금 칸 {structure_help[arr[i][j]]} 다음 칸 {structure_help[arr[ni][nj]]}')


            elif dj == -1:
                # 범위 안에 있고 다음칸이 왼쪽으로 갈수 있는 구조물일때,, 그리고 방문하지않은 곳이면
                if 0<= ni < N and 0<= nj <M and arr[ni][nj] in [1,3,4,5] and visited[ni][nj] == 0:
                    visited[ni][nj] = visited[i][j]+1
                    q.append((ni,nj))
                    # print(f'고,,지금 {i} {j} 새로운 위치 {ni} {nj} 방향 < 지금 칸 {structure_help[arr[i][j]]} 다음 칸 {structure_help[arr[ni][nj]]}')
        if flag == False:
            break
    # pprint.pprint(visited)
    cnt = 0
    for k in range(N):
        for m in range(M):
            if visited[k][m] != 0:
                cnt += 1
    return  cnt


import pprint


for tc in range(1, T+1):
    # 세로 크기 N, 가로 크기 M, 맨홀 뚜껑이 위치한장소의 세로 위치 R,
    # 가로 위치 C, 그리고 탈출 후 소요된 시간 L
    N,M,R,C,L = map(int,input().split())
    arr = [list(map(int, input().split())) for i in range(N)]

    print(f'#{tc} {bfs(R,C)}')
