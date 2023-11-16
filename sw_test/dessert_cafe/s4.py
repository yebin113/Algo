import sys
sys.stdin = open('input.txt')

def dfs(x,y,dir,path):
    global cnt
    # 방향이 다 꺾어지고, 원래자리로 돌아왔을떄..
    if dir == 3 and x == i and y == j:
        cnt = max(cnt,len(path))
        return

    if 0 <= x < N and 0<=y<N and str(arr[x][y]) not in path:
        dfs(x+dxy[dir][0],y+dxy[dir][1],dir,path+str(arr[x+dxy[dir][0]][y+dxy[dir][1]]))
        if dir < 3:
            dfs(x + dxy[dir+1][0], y + dxy[dir+1][1], dir+1, path + str(arr[x + dxy[dir+1][0]][y + dxy[dir+1][1]]))




T = int(input())

dxy = [[1,-1],[1,1],[-1,1],[-1,-1]]
for tc in range(1,T+1):
    cnt = 0
    # 한변의 길이 N
    N = int(input())
    # 디저트 지도
    arr = [list(map(int,input().split())) for _ in range(N)]
    for i in range(N-2):
        for j in range(1,N-1):

            visited = [[0]*N for _ in range(N)]
            path = dfs(i,j,0,'')

    print(f'#{tc} {cnt}')