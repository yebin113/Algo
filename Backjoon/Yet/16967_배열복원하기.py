H, W, X, Y = map(int, input().split())
B = []
for _ in range(H + X):
    B.append(list(map(int, input().split())))

A = [[0] * W for _ in range(H)]
for i in range(H):
    for j in range(W):
        if 0 <= i < X or 0 <= j < Y:
            A[i][j] = B[i][j]
        elif H-X <= i < H or W-Y <= j < W:
            A[i][j] = B[i+X-1][j+Y-1]
        # elif X <= i and Y <= j < 2 * Y or Y <= j and X <= i < X:
        #     A[i][j] = B[i][j] - B[i-X][j-Y]
    for k in range(H):
        print(A[k])
    print()
