import copy


def rotate1(arr):
    N = len(arr)
    M = len(arr[0])
    arr1 = copy.deepcopy(arr)
    for i in range(N // 2):
        for j in range(M):
            arr1[i][j], arr1[N - i-1][j] = arr1[N - i-1][j], arr1[i][j]
    return arr1


def rotate2(arr):
    N = len(arr)
    M = len(arr[0])
    arr1 = copy.deepcopy(arr)
    for i in range(N):
        for j in range(M//2):
            arr1[i][j], arr1[i][M - j-1] = arr1[i][M - j-1], arr1[i][j]
    return arr1


def rotate3(arr):
    N = len(arr)
    M = len(arr[0])
    new_arr = [[0]*N for _ in range(M)]
    for i in range(M):
        for j in range(N):
            new_arr[i][j] = arr[N - 1 - j][i]
    return new_arr


def rotate4(arr):
    N = len(arr)
    M = len(arr[0])
    new_arr = [[0] * N for _ in range(M)]
    for i in range(M):
        for j in range(N):
            new_arr[i][j] = arr[j][M-1-i]
    return new_arr


def rotate5(arr):
    N = len(arr)
    M = len(arr[0])
    new_arr = [[0] * M for _ in range(N)]
    # 1 -> 2
    for i in range(N // 2):
        for j in range(M // 2):
            new_arr[i][j + M // 2] = arr[i][j]
    # 2 -> 3
    for i in range(N // 2):
        for j in range(M // 2, M):
            new_arr[i + N // 2][j] = arr[i][j]
    # 3 -> 4
    for i in range(N // 2, N):
        for j in range(M // 2, M):
            new_arr[i][j - M // 2] = arr[i][j]
    # 4 -> 1
    for i in range(N // 2, N):
        for j in range(M // 2):
            new_arr[i - N // 2][j] = arr[i][j]
    return new_arr

def rotate6(arr):
    N = len(arr)
    M = len(arr[0])
    new_arr = [[0] * M for _ in range(N)]
    # 4 -> 3
    for i in range(N // 2, N):
        for j in range(M // 2):
            new_arr[i][j + M // 2] = arr[i][j]

    # 3 -> 2
    for i in range(N // 2, N):
        for j in range(M // 2, M):
            new_arr[i - N // 2][j] = arr[i][j]

    # 2 -> 1
    for i in range(N // 2):
        for j in range(M // 2, M):
            new_arr[i][j - M // 2] = arr[i][j]

    # 1 -> 4
    for i in range(N // 2):
        for j in range(M // 2):
            new_arr[i + N // 2][j] = arr[i][j]

    return new_arr


N, M, R = map(int, input().split())
array = []
for _ in range(N):
    array.append(list(map(int, input().split())))

orders = list(map(int,input().split()))
for order in orders:
    if order == 1:
        array = rotate1(array)
    elif order == 2:
        array = rotate2(array)
    elif order == 3:
        array = rotate3(array)
    elif order == 4:
        array = rotate4(array)
    elif order == 5:
        array = rotate5(array)
    elif order == 6:
        array = rotate6(array)

for i in range(len(array)):
    print(*array[i])
