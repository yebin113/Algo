"""
비상연락망과 연락을 시작하는 당번에 대한 정보가 주어질 때,
가장 나중에 연락을 받게 되는 사람 중 번호가 가장 큰 사람을 구하는 함수
"""

import sys
sys.stdin = open("input.txt")


def bfs(start):
    visited = [0]*(101)       # 방문기록
    q = [start]             # 큐
    visited[start] = 1
    end_list = []
    while q:
        now = q.pop(0)      # 현재 위치
        near_list = adj_l[now]  # 현재 위치에서 걸 수 있는 인접번호

        for near in near_list:  # 인접들을 순회
            if visited[near] == 0:  # 방문안한곳이면
                q.append(near)      # 큐에 넣고
                visited[near] = visited[now] + 1    # 방문표시 함 -> 얼마나 진행됐는가를 보려고
    return visited    # 방문리스트 리턴


T = 10

for tc in range(1, T + 1):
    N, start = map(int, input().split())  # 길이와 시작점
    arr = list(map(int, input().split()))  # 간선
    adj_l = [[] for i in range(101)]
    for i in range(len(arr) // 2):
        v1, v2 = arr[2 * i], arr[2 * i + 1]     # 방향성이 있음
        adj_l[v1].append(v2)
    finish_list = bfs(start)        # 방문리스트 받아오기
    max_contact = 0
    max_index = 0
    # 가장 긴 연락 길이? 를 가진 인덱스 추출
    for i in range(101):
        if max_contact <= finish_list[i]:
            max_contact = finish_list[i]
            max_index = i


    print(f'#{tc} {max_index}')
