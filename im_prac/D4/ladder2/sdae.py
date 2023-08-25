import sys
sys.stdin = open("input.txt")

T = 10

for case in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(100)]

    # 최소 거리와 최소 출발점 / 출발점 c
    min_distance = 10000
    min_start = 0
    for s in range(100):
        i = 0
        c = s
        # 이동 거리
        distance = 0
        if arr[0][c] == 1:
            visited = [[0] * 100 for _ in range(100)]
            # 도착하기 전까지 반복
            while i < 100:
                # 오른쪽에 1이 있으면 오른쪽으로 가고 방문 표시
                if 0 <= c + 1 < 100 and arr[i][c + 1] == 1 and visited[i][c + 1] == 0:
                    visited[i][c + 1] = 1
                    c += 1
                    distance += 1
                    # print(f"현재위치 {i}번째줄 {c}칸 -> 오른쪽으로 이동, 거리 {distance}")
                # 왼쪽도 마찬가지
                elif 0 <= c - 1 < 100 and arr[i][c - 1] == 1 and visited[i][c - 1] == 0:
                    visited[i][c - 1] = 1
                    c -= 1
                    distance += 1
                    # print(f"현재위치 {i}번째줄 {c}칸 -> 왼쪽으로 이동, 거리 {distance}")
                # 둘 다 아니면 아래로
                else:
                    if 0 <= i + 1 < 100:
                        visited[i + 1][c] = 1
                    i += 1
                    distance += 1
                    # print(f"현재위치 {i}번째줄 {c}칸 -> 아래으로 이동, 거리 {distance}")

        if distance > 0 and min_distance >= distance:
            min_distance = distance
            # print(min_distance, s)
            min_start = s


    print(f'#{case} {min_start}')