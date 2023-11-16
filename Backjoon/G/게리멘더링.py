from sys import stdin
from collections import deque

def bfs(start,group):
    q = deque()
    visited = deque()
    visited.append(start)
    q.append(start)

    while q:
        now = q.popleft()

        for next in arr[now]:
            if next not in visited and next in group:
                visited.append(next)
                q.append(next)
    if len(group)==len(visited):
        return True
    else:
        return False


# 구역의 개수
N = int(stdin.readline())
# 인구수
people = list(map(int,stdin.readline().split()))
# 1. 인접 리스트 만들기
arr = [[] for i in range(N + 1)]
min_cha = 100000000000000000
# N개의 줄에 각 구역에 인접한 정보
for i in range(1, N + 1):
    # 각 정보의 첫 번째 정수는 그 구역과 인접한 구역의 수
    arr_l = list(map(int, input().split()))
    for j in range(1, arr_l[0] + 1):
        # 인접한 구역의 번호가 주어짐 -> 인접 리스트 만들기
        arr[i].append(arr_l[j])
        arr[arr_l[j]].append(i)

# 2. 1~N번 지역을 부분집합으로 나누기
area = [i for i in range(1, N + 1)]

for i in range(1, 1 << (N - 1)):  # 공집합 제외, 중복되는 경우 제외
    g1 = []
    g2 = []
    g1_people = 0
    g2_people = 0


    for j in range(N):
        if i & (1 << j):
            g1.append(area[j])
        else:
            g2.append(area[j])

    # 3. 인접한지 확인하기
    if bfs(g1[0],g1) and bfs(g2[0],g2):
        hap_g1 = 0
        hap_g2 = 0
        for p in range(len(people)):
            if p + 1 in g1:
                hap_g1 += people[p]
            else:
                hap_g2 += people[p]
        # 갱신
        min_cha = min(min_cha,abs(hap_g1-hap_g2))

if min_cha > sum(people):
    print(-1)
else:
    print(min_cha)