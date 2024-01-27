from collections import deque

dir = {
    'Q': [[0, 1], [0, -1], [1, 0], [-1, 0], [1, 1], [1, -1], [-1, 1], [-1, -1]],
    'K': [[-1, -2], [-2, -1], [1, -2], [2, -1], [-1, 2], [-2, 1], [1, 2], [2, 1]]
}


def bfs(Q):
    q = deque(Q)
    while q:
        i, j = q.popleft()
        # 퀸이라면
        if board[i][j] == "Q":
            for di, dj in dir["Q"]:
                cant_go = False
                k = 1
                while 1:
                    ni = i + di * k
                    nj = j + dj * k
                    k += 1
                    if not (0 <= ni < N and 0 <= nj < M):
                        cant_go = True
                        break
                    if board[ni][nj] not in [0,1]:
                        break
                    board[ni][nj] = 1
                if cant_go:
                    continue
        else:
            for di, dj in dir["K"]:
                ni = i + di
                nj = j + dj
                if not (0 <= ni < N and 0 <= nj < M):
                    continue
                if board[ni][nj] not in [0,1]:
                    continue
                board[ni][nj] = 1


N, M = map(int, input().split())
board = [[0] * M for _ in range(N)]
q = deque()

Q, *Q_where = list(map(int, input().split()))
for i in range(len(Q_where) // 2):
    r, c = Q_where[2 * i] - 1, Q_where[2 * i + 1] - 1
    q.append((r, c))
    board[r][c] = "Q"

K, *K_where = list(map(int, input().split()))
for i in range(len(K_where) // 2):
    r, c = K_where[2 * i] - 1, K_where[2 * i + 1] - 1
    q.append((r, c))
    board[r][c] = "K"

P, *P_where = list(map(int, input().split()))
for i in range(len(P_where) // 2):
    r, c = P_where[2 * i] - 1, P_where[2 * i + 1] - 1
    board[r][c] = "P"

bfs(q)

cnt = 0
for i in range(N):
    cnt += board[i].count(0)
print(cnt)
