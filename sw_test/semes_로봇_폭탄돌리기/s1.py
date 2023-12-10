direction = {
    # 상우하좌 순서로 90도 회전
    0: [-1, 0],
    1: [0, 1],
    2: [1, 0],
    3: [0, -1]
}


def rotate(dir):
    dir += 1
    if dir == 4:
        dir = 0
    return dir


def turn():
    # 로봇들을 순회하며 robot_move를 호출하고 time을 늘려주는 역할
    global time
    for m in range(1, M + 1):
        # 죽은 로봇 넘기기
        if m in died:
            continue
        robot_move(m)
    time += 1
    # 생존시간 기록
    for m in range(1, M + 1):
        # 죽은 로봇 넘기기
        if m in died:
            continue
        robots[m]['survived_time'] = time
    return


def robot_move(robot):
    """
    인자로 받은 로봇을 움직여줌
    지금 설정되어있는 방향부터 네방향을 돌아가며 갈수 있는 곳인지
    can_go함수를 통해 확인 → 갈 수 있으면 움직여주기
    못가면 rotate 함수로 방향 돌리기
    움직인 위치가 폭탄이라면 해당 보드 위치를 0으로 바꿔주고 explode 호출
    """
    dir = robots[robot]['dir']
    can_move = False
    for d in range(4):
        di,dj = direction[dir]
        i, j = robots[robot]['l']
        i += di
        j += dj
        if can_go(robot,i,j):
            can_move = True
            robots[robot]['dir'] = dir
            break
        dir = rotate(dir)
    # 움직일 수 있는 위치라면
    if can_move:
        i, j = robots[robot]['l']
        # 폭탄 설치 가능하면 설치, 불가능하면 충전 시간 -1
        if robots[robot]['recharge'] == 0:
            board[i][j] = 'T'
            robots[robot]['recharge'] = 3
        else:
            board[i][j] = 0
            robots[robot]['recharge'] -= 1
        di,dj = direction[dir]
        ni = i+di
        nj = j+dj
        robots[robot]['l'] = [ni,nj]
        # 만약 움직인 위치가 폭탄이라면
        if board[ni][nj] == 'T':
            board[ni][nj] = 0
            explode(ni,nj)
        else:
            board[ni][nj] = f'{robot}'
    # 갈수 있는 곳이 없으면 가만히 있기
    else:
        return


def explode(i, j):

    # 어떤 로봇이 설치한 폭탄인지 찾고 삭제함(중복 점검 줄이기 위해)
    for m in range(1, M + 1):
        if [i, j] in robots[m]['traps']:
            robots[m]['traps'].remove([i, j])
            break
    for di, dj in [[-1, 0], [0, -1], [1, 0], [0, 1]]:
        for k in range(3):
            ni = i + di * k
            nj = j + dj * k

            # 범위 밖이거나 장벽을 만나면 더이상 폭발 X
            if not (0 <= ni < N and 0 <= nj < N) or (0 <= ni < N and 0 <= nj < N and board[ni][nj] == 1):
                break
            # 범위 안에 있을때
            elif 0 <= ni < N and 0 <= nj < N:
                # 또다른 폭탄을 만났을때 연쇄 폭발
                if board[ni][nj] == 'T':
                    board[ni][nj] = 0
                    explode(ni, nj)
                # 다른 로봇을 만났을때 고장냄
                elif board[ni][nj] != 0:

                    died.append(int(board[ni][nj]))
                    board[ni][nj] = 0


def can_go(robot, ni, nj):
    # 범위 밖이면 불가능
    if not(0<=ni<N and 0<=nj<N):
        return False
    # 내가 설치한 트랩이면 못감
    elif [ni,nj] in robots[robot]['traps']:
        return False
    # 장벽이면 못감
    elif board[ni][nj] == 1:
        return False
    else:
        # 내가 설치한 트랩들을 순회
        for ti,tj in robots[robot]['traps']:
            for di, dj in [[-1, 0], [0, -1], [1, 0], [0, 1]]:
                for k in range(1,3):
                    tni = ti + di * k
                    tnj = tj + dj * k
                    # 범위 밖이거나 장벽을 만나면 더이상 폭발 범위 x
                    if 0 <= tni < N and 0 <= tnj < N and board[tni][tnj] == 1:
                        break
                    # 범위 안에 내가 포함이 될때
                    if ni == tni and nj == tnj :
                        return False

    # 모두 통과할때 가능
    return True


T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(N)]
    robots = {}
    died = []
    for m in range(M):
        r, c, d = map(int, input().split())
        board[r][c] = f'{m + 1}'
        robots[m + 1] = {
            'l': [r, c],
            'dir': d,
            'recharge':0,
            'survived_time': 0,
            'traps': [],
        }
    time = 0
    for o in range(N):
        print(board[o])
    while 1:
        turn()
        print(time,'번 턴')
        for o in range(N):
            print(board[o])
        print('죽음',died)
        if time >= 5:
            break
        if len(died) >= M - 1:
            break

    print(f'#{tc}', end=' ')
    for m in range(1, M + 1):
        if m in died:
            print(robots[m]['survived_time'], end=' ')
        else:
            print(-1, end=' ')
    print()
