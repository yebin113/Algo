from collections import deque
from itertools import combinations
import copy

"""
라이브러리는 참 좋구나
1. 연구소 입력 받을때 빈칸과 바이러스를 배열에 기록
2. 빈칸중 3개를 벽으로 세울 조합으로 고름
3. 원래 연구소 정보를 deepcopy한 다음, 고른 세 빈칸을 벽을 친 다음 바이러스가 퍼지는 것을 직접 관리
    - 원래 visited 사용했는데 직접 기록하는 것이 더 편할거라 생각하고 변경
4. 최대 안전구역 갱신
"""
dir = [[0, 1], [-1, 0], [1, 0], [0, -1]]


def bfs(walls):
    arr2 = copy.deepcopy(area)
    global max_cnt
    q = deque()
    # 바이러스 큐에 담기
    for i,j in virus:
        q.append((i,j))
    # 고른 세개의 벽 세우기
    for di, dj in walls:
        arr2[di][dj] = 1

    # 바이러스 퍼뜨리기
    while q:
        i,j = q.popleft()
        for di, dj in dir:
            ni = i + di
            nj = j + dj
            if not(0<=ni<N and 0<=nj<M):
                continue
            if arr2[ni][nj] != 0:
                continue
            arr2[ni][nj] = 2
            q.append((ni,nj))

    # 안전구역 세고 갱신
    cnt = 0
    for i in range(N):
        for j in range(M):
            if arr2[i][j] == 0:
                cnt += 1
    max_cnt = max(max_cnt,cnt)



N,M = map(int,input().split())
max_cnt = 0
area = []
blank = []
virus = []
for i in range(N):
    line = list(map(int, input().split()))
    area.append(line)
    for j in range(M):
        # 빈칸 기록
        if line[j] == 0:
            blank.append((i,j))
        # 바이러스 기록
        elif line[j] == 2:
            virus.append((i,j))
# 빈칸중 세개의 벽 고르기
for walls in combinations(blank,3):
    bfs(walls)

print(max_cnt)