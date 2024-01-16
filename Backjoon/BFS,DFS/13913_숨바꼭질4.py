import sys
input = sys.stdin.readline
from collections import deque


def bfs(n,k):
    global ans, p
    q = deque([(n,[n])])
    if n > k:
        ans = n-k+1
        p = [i for i in range(n,k-1,-1)]
        return
    visited = [100001]*100001
    while q:
        locate, path = q.popleft()

        if locate == k:
            if ans > len(path):
                ans = len(path)
                p = path


        next_locate = [locate - 1, locate + 1, 2 * locate]
        # 지금 위치가 동생보다 크면 무조건 -1만
        if locate > k:
            next_locate = [locate - 1]

        for new in next_locate:
            # 현재 위치가 동생위치보다 크면 -1만 실행하기
            # 이미 경로에 있을때 패스
            if new in path:
                continue
            # 범위를 벗어나면 패스
            if not(0<=new<=100000):
                continue
            # 현재 위치 + 나랑 동생의 거리차 * 2 내에서 왔다 갔다 하기 위해 범위 제한
            if not(n-abs(n-k)*2 <= new <= n+abs(n-k)*2):
                continue
            # 현재의 visited 가 패스의 길이보다 길때만
            if visited[new] > len(path):
                # path에 추가
                # q에 현재 위치와 path 추가
                q.append((new,path+[new]))
                visited[new] = len(path)+1




N,K = map(int,input().split())
ans = 100000
p = []
bfs(N,K)
print(ans-1)
print(*p)