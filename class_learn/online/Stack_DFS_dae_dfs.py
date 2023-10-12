T = int(input())


# dfs에 대한 함수, n: 처음 시작할 곳 / V: 노드 개수 / arr_v: 노드가 표시된 배열
def dfs(n, V, arr_v):
    stack = []  # 스택 생성
    visited = [0] * (V + 1)  # 방문한 곳을 알 수 있는 visited 생성
    visited[n] = 1  # 시작점을 표시
    while True:
        # 오름차순으로 연결된 노드를 찾는다.
        for w in range(1, V + 1):
            # 현재 정점 n에 연결되어 있고 미방문한 w를 찾으면
            if arr_v[n][w] == 1 and visited[w] == 0:
                stack.append(n)  # 스택에 n을 쌓는다.
                n = w  # n은 다시 연결된 w로 갱신해준다.
                visited[n] = 1  # 연결된 지점에 방문 했다는 것을 표시
                break
        # # for 문이 끊기지 않고 모두 돌아간다면 - 맞는 w가 없다면 (for else 문)
        else:
            # 스택에 이미 지나온 노드가 있으면, 남아 있으면
            if stack:
                # 다시 스택을 제거해주면서 위로 올라가 다른 미방문한 w를 찾는다.
                n = stack.pop()
            # 스택에 아무것도 없으면 0으로 모두 돌았다는 것이므로 종료
            else:
                break
    return visited


for case in range(1, T + 1):
    V, E = map(int, input().split())  # V 개의 노드. E 개의 간선
    way_list = []  # [출발, 도착] 노드의 간선 정보
    for way in range(E):
        way_list.append(list(map(int, input().split())))
    S, G = map(int, input().split())  # 출발, 도착 노드

    arr_v = []  # V개의 점들이 간선으로 이어져 있는지 없는지를 표시할 arr
    for i in range(V + 1):
        arr_v.append([0] * (V + 1))

    # E개의 간선에서 way_list 로 알 수 있는 연결되어 있는 노드들을 arr_v에 1로 표시해준다.
    for e in range(E):
        v1, v2 = way_list[e][0], way_list[e][1]
        arr_v[v1][v2] = 1
        arr_v[v2][v1] = 1

    dfs(1, V, arr_v)
