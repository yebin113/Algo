N = int(input())
arr = [list(input()) for _ in range(N)]
check = [[0] * N for _ in range(N)]
dxy = [[-1, -1], [0, -1], [1, -1], [-1, 0], [0, 0], [1, 0], [-1, 1], [0, 1], [1, 1]]
no = 0
yes = 0
# 테두리 확인
for i in range(N):
    for j in range(N):
        if 1 <= i < N - 1 and 1 <= j < N - 1:
            continue
        num = int(arr[i][j])
        check[i][j] = num
        # 아닌 위치 찾기
        if num == 0:
            for di, dj in dxy:
                ni = i + di
                nj = j + dj
                if 1 <= ni < N - 1 and 1 <= nj < N - 1 and check[ni][nj] == 'yet':
                    check[ni][nj] = "x"
                    no += 1
        # 무조건 맞는 위치 고르기
        elif num == 3:
            for di, dj in dxy:
                ni = i + di
                nj = j + dj
                if 1 <= ni < N - 1 and 1 <= nj < N - 1:
                    check[ni][nj] = 1
                    yes += 1

import pprint



def check_find(check):
    for i in range(1, N - 1):
        for j in range(1, N - 1):
            if 2 <= i < N - 2 and 2 <= j < N - 2:
                check[i][j] = 1
                continue
            if check[i][j] == 1:
                for di, dj in dxy:
                    ni = i + di
                    nj = j + dj
                    # 테두리의 숫자
                    if ni == 0 or nj == 0 or ni == N - 1 or nj == N - 1:
                        check[ni][nj] -= 1
    pprint.pprint(check)


check_find(check)