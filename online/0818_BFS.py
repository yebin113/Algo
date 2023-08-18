"""
7 8
2 4 1 2 1 3 3 7 2 5 4 6 5 6 6 7
"""


def bfs(s, V):      # 시작점 s, 마지막 정점 v
    # visited 생성
    visited = [0] * (V+1)
    # 큐 생성
    Q = []
    # 시작점 인큐
    Q.append(s)
    # 시작점 방문표시
    visited[s] = 1
    # q에 정점이 남아있으면 => front != rear
    while Q:
        t = Q.pop(0)        # deQ
        print(t)            # 방문한 정점 출력
        # 인접한 정점중 인큐되지 않은 정점 w 있으면
        for w in adj_l[t]:
            if visited[w] == 0:
                # w 인큐, 인큐되었음을 표시
                Q.append(w)
                visited[w] = visited[t] + 1




V, E = map(int,input().split())     # 1번부터 V번 정점, E개의 간선
arr = list(map(int,input().split()))
# 인접리스트
adj_l = [[] for _ in range(V+1)]
for i in range(E):
    v1,v2 = arr[i*2], arr[2*i + 1]
    adj_l[v1].append(v2)
    adj_l[v2].append(v1)        # 방향이 없는경우
bfs(1,7)