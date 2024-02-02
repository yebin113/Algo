from collections import deque
def bfs(s,t):
    global cnt
    q = deque()
    q.append((s,t,0))
    while q:
        A, B, kick_cnt = q.popleft()
        if A == B:
            cnt = min(cnt,kick_cnt)
        else:
            if A*2 <= B+3:
                q.append((A*2,B+3,kick_cnt+1))
            if A+1 <= B:
                q.append((A+1, B, kick_cnt + 1))




C = int(input())
for _ in range(C):
    S, T = map(int,input().split())
    cnt = T-S
    bfs(S,T)
    print(cnt)