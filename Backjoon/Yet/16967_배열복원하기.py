H, W, X, Y = map(int, input().split())
B = []
for _ in range(H + X):
    B.append(list(map(int, input().split())))

A = [[0] * W for _ in range(H)]
for i in range(H):
    for j in range(W):
        A[i][j] = B[i][j]

for i in range(X, H):
    for j in range(Y, W):
        A[i][j] = B[i][j] - A[i - X][j - Y]
for k in range(H):
    print(*A[k])
# print()
