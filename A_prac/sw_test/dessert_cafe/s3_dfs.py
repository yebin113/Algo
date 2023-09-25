import sys

sys.stdin = open("input.txt")


def dfs(x,y,route,direction):
    global cnt
    #  방향이 마지막이고, 시작위치로 돌아왔으며 루트 길이가 2 이상일때
    if direction == 3 and x == i and y == j and len(route)>2:
        # 최댓값 갱신
        cnt = max(cnt,len(route))
        return
    # 범위안에 있고 이미 있지 않으면
    if 0<=x<N and 0<=y<N and arr[x][y] not in route:
        # 직진 할때의 재귀
        dfs(x+dir[direction][0], y+dir[direction][1],route+[arr[x][y]],direction)
        #  꺾을 방향이 남아있을때
        if direction < 3:
            # 꺾기 -> direction + 1 일때의 재귀
            dfs(x+dir[direction+1][0], y+dir[direction+1][1],route+[arr[x][y]],direction+1)


T = int(input())
# 좌하 -> 우하 -> 우상 -> 좌상
dir = [[1, -1],[1, 1] , [-1, 1],[-1, -1]]
for tc in range(1, T + 1):
    # 한변의 길이
    N = int(input())
    # 디저트 카페
    arr = [list(map(int, input().split())) for i in range(N)]
    cnt = 0
    # 열 2칸 전까지 가능함
    for i in range(N - 2):
        # 행 맨앞 맨뒤 안됨..
        for j in range(1, N - 1):
            dfs(i,j,[],0)
    if cnt == 0:
        cnt = -1
    print(f'#{tc} {cnt}')