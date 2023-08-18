"""
7 8
2 4 1 2 1 3 3 7 2 5 4 6 5 6 6 7

1. 시작 노드를 설정
2. 시작 노드를 Q에 삽입한다
3. 큐에서 노드를 하나씩 꺼내서, 해당 노드를 방문 처리하고 출력한다.
4. 방금 방문한 노드의 인접한 미방문 노드들을 모두 큐에 넣는다
5. 큐가 빌때까지 3,4를 반복수행한다

"""

def bfs(arr,start):
    # 방문 여부
    visited = set()
    # 시작 노드를 q에 삽입
    q = [start]
    # 큐가 빌때까지 반복
    while q:
        # 큐에서 노드를 꺼냄
        node = q.pop(0)
        # 방문여부 확인
        if node not in visited:
            # 방문 처리
            visited.add(node)
            print(node, end=' ')
            # 키값으로 접근
            neighbors = graph[node]     # 리스트 형태임
            for neighbor in neighbors:
                # 방문 안한 곳이면 큐에다가 넣음
                if neighbor not in visited:
                    q.append(neighbor)


# 인접행렬 -> 딕셔너리
# visited -> 세트

V, E = map(int, input().split())  # node, 간선
temp = list(map(int, input().split()))  # 연결정보
graph = {}

# 간선 정보 기록하기
for i in range(E):
    graph.setdefault(temp[2 * i], []).append(temp[2 * i + 1])
    graph.setdefault(temp[2 * i + 1], []).append(temp[2 * i])


# 탐색 시작(인접딕셔너리, 시작점)
bfs(graph, 1)