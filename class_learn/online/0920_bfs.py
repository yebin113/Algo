# 인접 행렬
graph = [
    [0, 1, 0, 1, 0],
    [1, 0, 1, 0, 1],
    [0, 1, 0, 0, 0],
    [1, 1, 0, 0, 1],
    [0, 1, 0, 1, 0]
]


def bfs(start):
    visited = [0] * 5
    # 먼저 방문 했던 것을 먼저 처리해야 한다
    queue = [start]
    visited[start] = 1
    # 큐가 빌때까지
    while queue:
        # 큐의 맨 앞 요소를 꺼냄
        now = queue.pop(0)
        print(now, end=' ')

        # 인접한 노드들을 큐에 추가
        for next in range(5):
            # 연결이 안되어 있다면 continue
            if graph[now][next] == 0:
                continue
            # 방문한 지점이면 큐에 추가하지 않음
            if visited[next] == 1:
                continue
            queue.append(next)
            visited[next] = 1
bfs(0)