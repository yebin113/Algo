from collections import deque
def bfs():
    global ans
    visited = [[0] * (W+2) for _ in range(H+2)]
    q = deque([(0,0)])
    while q:
        j,i = q.popleft()
        if j % 2 == 1:
            d = dir[1]
        else:
            d = dir[2]
        cnt = 0
        for dj, di in d:
            ni = i + di
            nj = j + dj
            # 범위 밖으로 나갈 경우
            if ni < 0 or nj >= W+2 or nj < 0 or ni >= H+2:
                continue
            else:
                print('범위 안 입니다.',ni,nj,W+2,H+2)
            if house[nj][ni] ==1 or visited[ni][nj] != 0:

                continue

            q.append((nj,ni))
            visited[ni][nj]  = 1

            cnt += 1
        ans += cnt




# 열(i)이 홀수일때, 열(i)이 짝수일때
dir = {
    1:[[0,-1],[1,-1],[1,0],[1,1],[0,1],[-1,0]],
    2:[[-1,-1],[0,-1],[1,0],[0,1],[-1,1],[-1,0]],
}
W,H = map(int, input().split())
house = [[0]*(W+2)]+[[0]+list(map(int,input().split()))+ [0] for _ in range(H)] + [[0] * (W+2)]
visited = [[0]*(W+2) for _ in range(H+2)]

ans = 0
bfs()
print(ans)