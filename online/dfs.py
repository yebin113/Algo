"""
# V E
# 간선정보
7 8
1 2 1 3 2 4 2 5 4 6 5 6 6 7 3 7
"""


def dfs(start, V, arr):
    # 방문리스트
    visited = [0] * (V + 1)
    # 스택
    stack = []
    # 시작점 체크하고 시작
    visited[start] = 1
    # 출발에 있으면
    while 1:
        for i in range(1, V + 1):
            # 다음에 갈 지점을 찾고, 방문하지 않은 곳에 닿으면
            if arr[start][i] == 1 and visited[i] == 0:
                # 스택에 쌓음
                stack.append(start)
                # 다음 위치로 옮김
                start = i
                # 방문 표시
                visited[start] = 1
                break

        # 다음에 갈 지점 못찾거나 방문한 정점이면
        else:
            # stack이 길이가 존재할때
            if len(stack) != 0:
                # pop
                start = stack.pop()
            # 스택이 없으면 다 돈거니까 탈출~
            else:
                break
    # 방문 리스트 리턴
    return visited


V, E = map(int, input().split())  # 1번 부터 V번 정점, E개의 간선
data = list(map(int, input().split()))  # 간선정보

arr = [[0] * (V + 1) for i in range(V + 1)]
visited = [0] * (V + 1)  # 노드의 방문여부 체크 리스트

for i in range(E):
    n1, n2 = [data[2 * i], data[2 * i + 1]]
    arr[n1][n2] = 1  # n1과 n2는 인접해있다
    arr[n2][n1] = 1  # 무방향성이라 둘다 추가해줌
print(dfs(1,V,data))
#
# # 재귀
# def dfs(v):  # 시작점
#     visited[v] = 1
#     print(v, end=' ')  # 특정 로직을 수행하는 것
#
#     # v -> 현재 시작 정점, 인접한 정점 중에서 방문을 하지 않은 곳
#     for w in range(1, V + 1):
#         if arr[v][w] == 1 and visited[w] == 0:
#             dfs(w)
#
#
#
# # 반복
# def dfs2(v):
#     stack = [v]     # 방문한곳들 (시작점)
#     # 스택이 빌때까지 반복
#     while len(stack):
#         v = stack.pop()
#         print(v, end=' ')
#         visited[v]= 1
#         for w in range(1,V+1):
#             if arr[v][w] == 1 and visited[w] ==0:
#                 stack.append(w)
#
# dfs2(1)
