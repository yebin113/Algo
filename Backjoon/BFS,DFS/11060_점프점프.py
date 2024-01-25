from collections import deque
def bfs():
    global check
    q = deque()
    q.append((0,0))
    visited[0] = 0
    while q:
        i, cnt = q.popleft()

        if i >= N-1:
            visited[-1] = min(cnt+1,visited[-1])
            check = True
        else:
            visited[i] = min(visited[i], cnt)
            for di in range(1,arr[i]+1):
                ni = i + di
                q.append((ni,cnt+1))


N = int(input())
arr = list(map(int,input().split()))
check = False
visited = [1001]*N
bfs()
if check == False:
    print(-1)
else:
    print(visited[-1]-1)