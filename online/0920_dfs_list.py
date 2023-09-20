# 인접 리스트
# 주의사항 (각 노드마다 갈 수 있는 지점의 개수가 다름)
# range index 문제가 생길 수 있지만 메모리 적으로 이득
graph = [
    [1, 3],
    [0, 2, 3, 4],
    [1],
    [0, 3, 4],
    [1, 3]
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
        for to in range(len(graph[now])-1,-1,-1):
            next = graph[now][to]
            # 방문한 지점이라면 stack에 추가하지 않음
            if next in visited:
                continue
            stack.append(next)
    # 출력을 위한 반환
    return visited


print('dfs stack is', *dfs_stack(0))

# DFS 재귀 버전
# map 크기길이를 알때
visited = [0] * 5
path = []


def dfs(now):
    visited[now] = 1  # 현재지점 방문 표시
    path.append(now)

    # 인접한 노드들을 방문
    for to in range(len(graph[now])):
        next = graph[now][to]
        if visited[next]:
            continue
        dfs(next)
    return path


print('dfs 재귀 :', *dfs(0))
