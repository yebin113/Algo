import sys
sys.stdin = open("input.txt")
import heapq
T = int(input())

def dij(start):
    global distance
    # 2. 우선순위 큐
    pq = []
    heapq.heappush(pq, (0, start))
    # 출발점은 거리가 0
    distance[start] = 0

    while pq:
        # 현재 시점에서 누적 거리가 가장 짧은 노드에 대한 정보 꺼내기
        dist, now = heapq.heappop(pq)
        # 이미 방문한 지점 + 누적 거리가 더 짧게 방문한 적이 있다면 pass
        if distance[now] < dist:
            continue
        # 인접 노드들을 확인
        for next in graph[now]:

            next_node = next[1][0]*N + next[1][1]
            cost = next[0]

            # next node로 가기 위한 누적 거리
            new_cost = dist + cost
            # 누적거리가 기존보다 클때 pass
            if distance[next_node] <= new_cost:
                continue
            distance[next_node] = new_cost
            heapq.heappush(pq, (new_cost, next_node))


dxy = [[0,1],[1,0],[-1,0],[0,-1]]
for tc in range(1, T+1):
    # 지도의 크기
    N = int(input())
    # 지도
    arr = [list(map(int, input())) for _ in range(N)]
    distance = [int(1e9)]*(N*N)
    graph = [[] for i in range(N*N)]
    # 인접 리스트 만들기
    for i in range(N):
        for j in range(N):
            for di, dj in dxy:
                ni = i + di
                nj = j + dj
                # 범위를 벗어나면 넘기기
                if ni < 0 or ni >= N or nj < 0 or nj >= N:
                    continue
                # 다음위치의 가중치와 다음위치
                graph[i*N+j].append([arr[ni][nj],(ni,nj)])
    dij(0)


    print(f'#{tc} {distance[-1]}')