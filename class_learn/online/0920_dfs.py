# 인접 행렬
graph = [
    [0, 1, 0, 1, 0],
    [1, 0, 1, 0, 1],
    [0, 1, 0, 0, 0],
    [1, 1, 0, 0, 1],
    [0, 1, 0, 1, 0]
]


# 인접 리스트


# DFS 스택버전

def dfs_stack(start):
    stack = [start]
    visited = []
    while stack:
        now = stack.pop()
        # 이미 방문했다면 continue
        if now in visited:
            continue
        # 방문하지 않은 지점이라면, 방문표시
        visited.append(now)
        # 갈 수 있는 곳들을 stack에 추가
        for next in range(4,-1,-1):
            # 연결이 되어있다면 continue
            if graph[now][next] == 0:
                continue
            # 방문한 지점이라면 stack에 추가하지 않ㅇ믐
            if next in visited:
                continue
            stack.append(next)
    # 출력을 위한 반환
    return visited


print('dfs stack :', *dfs_stack(0))


# DFS 재귀 버전
# map 크기길이를 알때
visited = [0]*5
path = []

def dfs(now):
    visited[now] = 1    # 현재지점 방문 표시
    path.append(now)

    # 인접한 노드들을 방문
    for next in range(5):
        if graph[now][next] == 0:
            continue
        if visited[next]:
            continue
        dfs(next)
    return path
print('dfs 재귀 :',*dfs(0))
