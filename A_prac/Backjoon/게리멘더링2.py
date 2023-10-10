from sys import stdin
import pprint
dxy = [[1, -1], [1, 1], [-1, 1], [-1, -1]]

def dfs(x,y,route,direction):
    global g1,g2,g3,g4,g5,min_cha
    visited = [[0]*N for _ in range(N)]
    #  방향이 마지막이고, 시작위치로 돌아왔으며 루트 길이가 2 이상일때
    if direction == 3 and x == i and y == j and len(route)>2:
        print(route)
        for k in range(N):
            for m in range(N):
                # 겉에 사각형
                if k < route[0][0]:
                    if m <= route[0][1]:
                        g1 += data[k][m]
                    else:
                        g2 += data[k][m]
                elif k > route[2][0]:
                    if m <= route[2][1]:
                        g3 += data[k][m]
                    else:
                        g4 += data[k][m]
                elif m < route[1][1]:

                    if k < route[1][0]:
                        g1 += data[k][m]
                    else:
                        g3 += data[k][m]
                elif m > route[3][1]:
                    if k <= route[3][0]:
                        g2 += data[k][m]
                    else:
                        g4 += data[k][m]

                # 안의 마름모
                elif k < route[0][0] and m < route[0][1] and k+m < route[1][1]+route[1][0]:
                    g1 += data[k][m]
                elif k > route[0][0] and m < route[0][1] and route[0][1]+route[0][0] < k+m <route[3][0]+route[3][1]:
                    g3 += data[k][m]
                elif k > route[0][0] and m > route[0][1] and k+m > route[3][0]+route[3][1]:
                    g4 += data[k][m]
                elif k < route[0][0] and m > route[0][1] and route[0][1]+route[0][0] < k+m <route[3][0]+route[3][1]:
                    g2 += data[k][m]
                else:
                    g5 += data[k][m]
                    visited[k][m] = 1
        pprint.pp(visited)
        if g1 != 0 and g2 != 0 and g3 != 0 and g4 != 0 and g5 != 0:
            max_g = max(g1,g2,g3,g4,g5)
            min_g = min(g1, g2, g3, g4, g5)
            min_cha = min(min_cha,max_g-min_g)
            return
    # 범위안에 있고 이미 있지 않으면
    if 0<=x<N and 0<=y<N:
        # 직진 할때의 재귀
        nx = x + dxy[direction][0]
        ny = y + dxy[direction][1]
        dfs(nx,ny,route,direction)
        #  꺾을 방향이 남아있을때
        if direction < 3:
            # 꺾기 -> direction + 1 일때의 재귀
            dfs(x+dxy[direction+1][0], y+dxy[direction+1][1],route+[(x,y)],direction+1)


N = int(stdin.readline())
data = []
for _ in range(N):
    data.append(list(map(int, stdin.readline().split())))

min_cha = int(1e9)
for i in range(N):
    for j in range(N):
        g1 = 0
        g2 = 0
        g3 = 0
        g4 = 0
        g5 = 0
        dfs(i, j, [(i,j)],0)

print(min_cha)