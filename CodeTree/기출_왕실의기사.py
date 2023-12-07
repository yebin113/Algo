def move(knight, dir):
    visited[knight] = 1
    """
    :param knight: 기사 번호 
    :param dir: 방향
    """
    di = direct[dir][0]
    dj = direct[dir][1]
    ni = knights_info[knight]['r'] + di
    nj = knights_info[knight]['c'] + dj
    h = knights_info[knight]['h']
    w = knights_info[knight]['w']

    # 새로운 위치 범위 탐색
    for i in range(ni, ni + h):
        for j in range(nj, nj + w):
            # 범위 밖으로 나가거나 벽을 만나면 못움직임
            if not (0 <= i < L and 0 <= j < L) or board[i][j] == 2:
                return False
            else:
                for k in range(1, N + 1):
                    r1 = knights_info[k]['r']
                    c1 = knights_info[k]['c']
                    h1 = knights_info[k]['h']
                    w1 = knights_info[k]['w']
                    # 죽었거나 지금 검사하는 기사거나, 이미 이동한 기사면 패스
                    if k in die or k == knight or visited[k] != 0:
                        continue
                    # 지금 기사와 겹치면 재귀로 이동가능한지 확인
                    elif r1 <= i <= r1 + h1 - 1 and c1 <= j <= c1 + w1 - 1:
                        if move(k, dir) == False:
                            return False
    # 통과하면 True
    return True


def damage(ordered, dir):
    """
    실제 이동과 데미지 체크
    :param ordered: 명령받은 기사는 빼고 데미지
    :param dir: 방향
    """
    di = direct[dir][0]
    dj = direct[dir][1]
    for k in range(1, N + 1):
        if visited[k] == 0:
            # 안움직인 기사 건너뛰기
            continue
        # 이동
        knights_info[k]['r'] += di
        knights_info[k]['c'] += dj
        r = knights_info[k]['r']
        c = knights_info[k]['c']
        h = knights_info[k]['h']
        w = knights_info[k]['w']
        # 명령받은 사람이랑 죽은사람은 데미지 체크 X
        if k == ordered or k in die:
            # print(f'{k}번 기사는 이미 움직이거나 죽었다')
            continue
        for i in range(r, r + h):
            check = False
            for j in range(c, c + w):
                if not(0<=i<L and 0<=j<L):
                    knights_info[k]['damaged'] += knights_info[k]['power']

                # 함정일경우 데미지
                if 0<=i<L and 0<=j<L and board[i][j] == 1:
                    knights_info[k]['damaged'] += 1
                if knights_info[k]['power'] - knights_info[k]['damaged'] <= 0:
                    die.append(k)
                    check = True
                    break
            if check:
                break


direct = {
    0: [-1, 0],
    1: [0, 1],
    2: [1, 0],
    3: [0, -1]
}
L, N, Q = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(L)]
# for i in range(L):
#     print(board[i])
knights_info = {}
die = []
for m in range(N):
    r, c, h, w, k = map(int, input().split())
    knights_info[m + 1] = {
        'r': r - 1,
        'c': c - 1,
        'h': h,
        'w': w,
        'power': k,
        'damaged': 0
    }
    # print(knights_info[m+1])
# print()
for i in range(Q):
    visited = [0] * (N + 1)
    num, dir = map(int, input().split())
    # print(f'{num}번 기사 {direct[dir]}방향으로')
    if num in die or not move(num,dir):
        # print('못움직입')
        # for k in range(1,N+1):
        #     print(knights_info[k])
        # print()
        continue
    # print('움직인 기사',visited)
    damage(num,dir)
    # for k in range(1,N+1):
    #     print(knights_info[k])
    # print()
total = 0
for k in range(1,N+1):
    if k in die:
        continue
    total += knights_info[k]['damaged']
print(total)

