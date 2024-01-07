import sys
input = sys.stdin.readline

def rotate(dir):
    dir += 1
    if dir == 4:
        dir = 0
    return dir


def dfs(i,j):
    # print(f'시작 위치 {i,j}')
    path = []
    # 맨 처음 오른쪽
    d = 0
    ni, nj = i, j
    while 0 <= ni < N and 0 <= nj < M:
        if visited[ni][nj] != d and (ni,nj,d) not in path:
            path.append((ni,nj,d))
        else:
            answer.append(i+1)
            for ri,rj,dd in path:
                visited[ri][rj] = dd
            return

        k = arr[ni][nj]
        ni += dir[d][0] * k
        nj += dir[d][1] * k
        d = rotate(d)


dir = [[0,1],[1,0],[0,-1],[-1,0]]

N,M = map(int, input().split())
arr = []
for _ in range(N):
    a = list(map(int,input().split()))
    arr.append(a)
visited = [[5]*M for _ in range(N)]
answer = []
res = []
for i in range(N):
    dfs(i,0)


print(len(answer))
if len(answer):
    print(*answer)
