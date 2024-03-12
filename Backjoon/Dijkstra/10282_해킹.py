import sys
import heapq 
input = sys.stdin.readline


def dijkstra(start, infect, graph):
    heapq.heappush(heap, [0, start])
    infect[start] = 0
    while heap:
        now_time, now = heapq.heappop(heap)
        for to, nect_time in graph[now]:
            new_time = nect_time + now_time
            if new_time < infect[to]:
                infect[to] = new_time
                heapq.heappush(heap, [new_time, to])

T = int(input())
for _ in range(T):
    N, D, C = map(int ,input().split())
    graph = [[] for _ in range(N + 1)]
    infect = [100000000000] * (N + 1)
    heap = []
    for _ in range(D):
        a, b, s = map(int, input().split())
        graph[b].append([a, s])

    dijkstra(C, infect, graph)

    cnt = 0
    time = 0
    for i in infect:
        if i != 100000000000:
            cnt += 1
            time = max(time, i)

    print(f"{cnt} {time}")