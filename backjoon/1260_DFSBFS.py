def dfs(start):
    visited.append(start)
    for i in range(len(arr[start])):
        if arr[start][i] in visited:
            continue
        dfs(arr[start][i])
    return visited




def bfs(start):
    visited = [start]
    q = [start]

    while q:
        i = q.pop(0)
        for next in arr[i]:
            if next not in visited:
                q.append(next)
                visited.append(next)
    return visited


# 정점의 개수 N(1 ≤ N ≤ 1,000), 간선의 개수 M(1 ≤ M ≤ 10,000), 탐색을 시작할 정점의 번호 V
N,M,V = map(int,input().split())
# 인접 리스트
arr = [[] for _ in range(N+1)]
# M개의 줄에는 간선이 연결하는 두 정점의 번호
for _ in range(M):
    f,t = map(int,input().split())
    # 양방향
    arr[f].append(t)
    arr[t].append(f)
    # 빠른 번호 순서대로 순회해야 해서..
    arr[f].sort()
    arr[t].sort()

visited = []
stack = []
print(*dfs(V))
print(*bfs(V))
