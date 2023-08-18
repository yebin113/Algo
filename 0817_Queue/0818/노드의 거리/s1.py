import sys
sys.stdin = open("input.txt")


def bfs(start, end):

    visited = [0] * (V + 1)     # 방문리스트를 만든다
    q = [start]                      # 시작점이 들어간 큐를 만든다
    cnt = 1
    while q:                    # q가 없어질때까지 반복
        next = q.pop(0)         # 큐의 맨 앞값을꺼냄
        for near in adj_l[next]:    # 방문처리한 정점의 인접리스트를
            if visited[near] == 0:  # 방문했는지 확인 후 안했으면
                q.append(near)      # 모두 큐에 넣습니다
                visited[near] = visited[next] + 1   # 그리고 여기서 방문처리(위에서 안해도됨)
    return visited[end]

T = int(input())

for tc in range(1, T+1):
    # 정점과 간선의 개수
    V, E = map(int, input().split())
    adj_l = [[] for _ in range(V+1)]    # 인접인덱스를 저장할 리스트
    for i in range(E):
        v1,v2 = map(int,input().split())
        adj_l[v1].append(v2)
        adj_l[v2].append(v1)        # 방향성이 없다

    # 시작과 끝 노드
    start, end = map(int,input().split())


    print(f'#{tc} {bfs(start,end)}')