# M은 상자의 가로 칸의 수, N은 상자의 세로 칸
M, N = map(int, input().split())
# 정수 1은 익은 토마토, 정수 0은 익지 않은 토마토, 정수 -1은 토마토가 들어있지 않은 칸
tomatoes = [list(map(int, input().split())) for _ in range(N)]
day = 0

dxy = [[0, -1], [-1, 0], [0, 1], [1, 0]]

# 저장될 때부터 모든 토마토가 익어있는 상태이면 0을 출력해야 하고
flag = True

# 토마토가 모두 익지는 못하는 상황이면 -1을 출력
for i in range(N):
    # 익은 토마토가 없는 경우 체크
    if tomatoes[i].count(1) != 0:
        flag = False
        break
import pprint
# 익은 토마토가 없다면 익을 수 없음..
if flag:
    day = -1
#
else:
    while True:

        change = 0
        # 익은 토마토가 있는 장소를 찾는다
        for i in range(N):
            for j in range(M):
                if tomatoes[i][j] == 1:
                    # 델타 네방향을 찾는다
                    for di, dj in dxy:
                        ni = i + di
                        nj = j + dj
                        # 새로운 인덱스가 범위 안에 있고, 익지 않았으며, -1이 아닐때
                        if 0 <= ni < N and 0 <= nj < M and tomatoes[ni][nj] == 0:
                            # 주변 토마토가 익는다
                            tomatoes[ni][nj] = 1
                            change += 1
        pprint.pprint(tomatoes)

        if change == 0:
            break
        day += 1

    # 만약 다 했는데 못익은 토마토가 존재하면..
    for i in range(N):
        # 안익은 토마토 존재???
        if tomatoes[i].count(0) != 0:
            day = -1
            break

# 토마토가 모두 익을 때까지의 최소 날짜
print(day)
