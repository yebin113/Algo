from sys import stdin
import pprint

dxy = [[1, -1], [1, 1], [-1, 1], [-1, -1]]


def dfs(x, y, route, direction):
    global min_cha
    visited = [[0] * N for _ in range(N)]

    #  방향이 마지막이고, 시작위치로 돌아왔으며 꼭짓점이 4개일때
    if direction == 3 and x == i and y == j and len(route) == 4:
        g1 = 0
        g2 = 0
        g3 = 0
        g4 = 0
        g5 = 0
        startx = route[0][0]
        starty = route[0][1]
        d1 = abs(route[1][0] - route[0][0])
        d2 = abs(route[3][1] - route[0][1])
        # 범위에 따라 다르게 더한다
        # visited는 범위 맞나 확인하려고 사용!
        for r in range(N):
            for c in range(N):
                if r < startx + d1 and c <= starty and r + c < route[0][0] + route[0][1]:
                    g1 += data[r][c]
                    visited[r][c] += 1
                elif r <= startx + d2 and starty < c < N and r - route[0][0] < c - route[0][1]:
                    g2 += data[r][c]
                    visited[r][c] += 2
                elif startx + d1 <= r < N and c < starty - d1 + d2 and r - route[1][0] > c - route[1][1]:
                    g3 += data[r][c]
                    visited[r][c] += 3
                elif startx + d2 < r < N and starty - d1 + d2 <= c < N and r + c > route[3][0] + route[3][1]:
                    g4 += data[r][c]
                    visited[r][c] += 4
                else:
                    g5 += data[r][c]
                    visited[r][c] += 5
        # 갱신하기
        if g1 != 0 and g2 != 0 and g3 != 0 and g4 != 0 and g5 != 0:
            group = [g1, g2, g3, g4, g5]
            min_cha = min(min_cha, max(group) - min(group))
            return
    # 범위안에 있고 이미 있지 않으면
    if 0 <= x < N and 0 <= y < N:
        # 직진 할때의 재귀
        nx = x + dxy[direction][0]
        ny = y + dxy[direction][1]
        dfs(nx, ny, route, direction)
        #  꺾을 방향이 남아있을때
        if direction < 3:
            # 꺾기 -> direction + 1 일때의 재귀
            dfs(x + dxy[direction + 1][0], y + dxy[direction + 1][1], route + [(x, y)], direction + 1)


N = int(stdin.readline())
data = []
for _ in range(N):
    data.append(list(map(int, stdin.readline().split())))

min_cha = int(1e9)
for i in range(N):
    for j in range(N):
        dfs(i, j, [(i, j)], 0)

print(min_cha)
