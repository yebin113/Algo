
def knock_down(i, j, direction):
    if [i,j] not in q:
        q.append([i,j])
    cnt = board[i][j]
    visited[i][j] = "F"

    for k in range(1, cnt):
        ni = i + dir[direction][0] * k
        nj = j + dir[direction][1] * k
        if not (0 <= ni < N and 0 <= nj < M):
            continue
        if [ni, nj] not in q:
            q.append([ni, nj])
        if board[ni][nj] > 1 and visited[ni][nj] == "S":
            knock_down(ni, nj, direction)
        visited[ni][nj] = "F"





N, M, R = map(int, input().split())
board = []
for _ in range(N):
    board.append(list(map(int, input().split())))


visited = [['S']*M for _ in range(N)]
dir = {'N': [-1, 0], 'S': [1, 0], 'W': [0, -1], 'E': [0, 1]}
point = 0


for _ in range(R):
    q = []
    attack = list(map(str, input().split()))
    attack[0] = int(attack[0]) - 1
    attack[1] = int(attack[1]) - 1
    if visited[attack[0]][attack[1]] == 'S':
        knock_down(*attack)
    save = list(map(int, input().split()))
    save[0] -= 1
    save[1] -= 1
    # 세울 부분 도미노 개수를 미리 저장해둠 -> 공격할때 쓰러지면 0 만들꺼라..
    save_cnt = board[save[0]][save[1]]
    visited[save[0]][save[1]] = "S"
    board[save[0]][save[1]] = save_cnt

    if save in q:
        point += len(q) -1
    else:
        point += len(q)


print(point)
for i in range(N):
    print(*visited[i])
