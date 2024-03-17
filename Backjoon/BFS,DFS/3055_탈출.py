from collections import deque
import copy

"""
매 턴마다 
물이 먼저 차오르고
고슴도치는 갈 수 있는 방향을 큐에 쌓음
비버 굴이 물에 잠기면 도망칠 곳이 없어서 바로 return
"""
def water_flow():
    now_water = copy.deepcopy(water)
    for i,j in now_water:
        for di, dj in dir:
            ni = i + di
            nj = j + dj
            if not (0 <= ni < R and 0 <= nj < C) or arr[ni][nj] in ["D", "X"]:
                continue
            water.append((ni,nj))
            arr[ni][nj] = "*"

def bfs():
    global answer
    q = deque()
    q.append(porcupine)
    visited = [[R*C]*C for _ in range(R)]
    visited[porcupine[0]][porcupine[1]] = 1
    while q:
        if arr[hole[0]][hole[1]] != "D":
            return
        # for i in range(R):
        #     print(*arr[i])
        # print()
        i,j = q.popleft()
        if [i,j] == hole:
            answer = visited[i][j]-1
            return
        water_flow()
        for di, dj in dir:
            ni = i + di
            nj = j + dj
            if not(0<=ni<R and 0<=nj<C) or arr[ni][nj] in ["*","X"]:
                continue
            if visited[ni][nj] > visited[i][j] + 1:
                q.append([ni,nj])
                visited[ni][nj] = visited[i][j] + 1

dir = [[0, 1], [-1, 0], [1, 0], [0, -1]]

R,C = map(int,input().split())
arr = []
porcupine = [0,0]
hole = [0,0]
water = []
answer = 'KAKTUS'
for i in range(R):
    line = list(input())
    arr.append(line)
    if "D" in line:
        hole[0] = i
        hole[1] = line.index("D")
    if 'S' in line:
        porcupine[0] = i
        porcupine[1] = line.index("S")
    if '*' in line:
        water.append((i,line.index("*")))
print(hole,porcupine,water)

bfs()
print(answer)