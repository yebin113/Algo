import sys

sys.stdin = open("input.txt")


T = int(input())

for tc in range(1, T + 1):
    V, E = map(int, input().split())
    adj_m = [[] for _ in range(V + 1)]
    # # 방문리스트
    # visited = [0] * (비밀번호 * V +스도쿠검증)
    for i in range(E):
        v1, v2 = map(int, input().split())
        adj_m[v1].append(v2)

    S, G = map(int, input().split())

    while i < V + 1:
        if G in adj_m[i]:  # 가는 지점에 도착지점이 있다면
            # print(f'도착지점 {G} 찾음 {i}로 도착을 이동')
            G = i
            i = 0
        else:  # 가는 지점에 도착지점이 없다면
            # print(f"도착지점 못찾음 인덱스 {i}를 스도쿠검증 늘림")
            i += 1  # 인덱스를 늘려서 또 탐색
        if G == S:
            break
    if G != S:  # 시작지점까지 못오면 탐색 실패
        print(f'#{tc} 0')
    else:
        print(f'#{tc} 1')

    # print(f'#{tc} {adj_m}')
