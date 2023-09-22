import sys

sys.stdin = open("input.txt")
import heapq

T = int(input())


def dij(start, end):
    pq = []
    # 첫 시작 값과 시작 위치를 넣어준다..
    heapq.heappush(pq, (0, start))
    distance[start] = 0
    while pq:
        dist, now = heapq.heappop(pq)
        # 끝에 도달했다면 거리를 반환
        if now == end:

            return dist
        # 만약 저장되어있는 거리가 지금 거리보다 짧으면 스루
        if distance[now] < dist:
            continue
        # 인접 리스트를 순회하며
        for next in graph[now]:
            # 다음노드
            next_node = next[1]
            # 다음 노드로 가는 가중치
            time = next[0]
            # 누적
            new_time = dist + time
            # 저장되어있는 값이랑 비교해서 갱신
            if distance[next_node] <= new_time:
                continue
            distance[next_node] = new_time
            # 새로운 노드와 새로운 시간을 저장
            heapq.heappush(pq, (new_time, next_node))

    return distance[end]


for tc in range(1, T + 1):
    N, M, X = map(int, input().split())
    graph = [[] for i in range(N + 1)]
    for _ in range(M):
        f, t, w = map(int, input().split())
        # 단방향
        graph[f].append([w, t])
    max_dis = 0

    # 생일자의 집
    for i in range(N):
        dis_now = 0
        # 움직여야 하는 주민
        for j in range(N):
            # 생일자는 움직일 필요가 없어요
            if i == j:
                continue
            # 거리 초기화(최솟값을 구할것..)
            distance = [int(1e9)] * (N+1)
            go_to = dij(i,j)
            come_back = dij(j,i)

            # 최댓값 갱신
            if max_dis < go_to:
                max_dis = go_to

            if max_dis < come_back:
                max_dis = come_back


    print(f'#{tc} {max_dis}')
