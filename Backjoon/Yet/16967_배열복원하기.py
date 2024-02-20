H, W, X, Y = map(int, input().split())
B = []
for _ in range(H + X):
    B.append(list(map(int, input().split())))

A = [[0] * W for _ in range(H)]
for i in range(H):
    for j in range(W):
        # 왼쪽, 위
        if 0 <= i < X or 0 <= j < Y:
            print(i,j,'왼쪽위')
            A[i][j] = B[i][j]
        # 오른쪽, 아래
        elif H-X <= i < H or W-Y <= j < W:
            print(i, j, '오른쪽 아래')
            A[i][j] = B[i+X][j+Y]
        # 중간
        elif Y <= j < 2 * Y or X <= i < 2 * X:
            print(i,j, Y, 2*Y, X, 2*X)

            A[i][j] = B[i][j] - B[i-X][j-Y]
        # else:
        #     A[i][j] = B[i + X][j + Y] - B[i][j]

    for k in range(H):
        print(*A[k])
    print()
