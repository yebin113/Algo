dir_dict = {
    1: [0, -1],
    2: [-1, -1],
    3: [-1, 0],
    4: [-1, 1],
    5: [0, 1],
    6: [1, 1],
    7: [1, 0],
    8: [1, -1]
}

diagonal = [[-1, -1], [1, -1], [-1, 1], [1, 1]]
N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
basket = [[0] * N for _ in range(N)]
clouds = [(N - 1, 0), (N - 1, 1), (N - 2, 0), (N - 2, 1)]
for _ in range(M):
    direction, distance = map(int, input().split())
    print('이동전 구름',clouds)
    # 각 구름을 순회하며
    for i in range(len(clouds)):
        # d방향으로 s만큼 이동
        ni = clouds[i][0] + dir_dict[direction][0] * distance
        nj = clouds[i][1] + dir_dict[direction][1] * distance
        while ni >= N:
            ni -= N
        while nj >= N:
            nj -= N
        while ni < 0:
            ni += N
        while nj < 0:
            nj += N


        arr[ni][nj] += 1

        # 구름 이동
        clouds[i] = (ni,nj)

        # 물복사
        water_cnt = 0
        for di, dj in diagonal:
            nni = ni + di
            nnj = nj + dj
            if 0 < nni <= N and 0 <= nnj < M:
                water_cnt += 1
        arr[ni][nj] += water_cnt
    print('이동 후 구름', clouds)
    next_clouds = []
    print(' 구름 생기기전 물 양')
    for i in range(N):
        print(arr[i])
    for i in range(N):
        for j in range(N):
            if arr[i][j] >= 2 and (i, j) not in clouds:
                next_clouds.append((i, j))
                arr[i][j] -= 1

    clouds = next_clouds
    print('새로 생긴 구름', clouds)
    print(' 구름 생 긴 후 물 양')
    for i in range(N):
        print(arr[i])
print(sum(sum(arr,[])))