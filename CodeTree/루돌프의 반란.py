def distance(one,two):
    # 좌표 두개를 받아서 사이 거리를 알려주는 함수
    return (one[0]-two[0])**2+(one[1]-two[1])**2


def order():
    global all_santa_die
    min_dis = N*N*2
    maxi = 0
    maxj = 0
    near_santa = 0
    # 가장 가까운 산타 고르기
    for s in range(1,P+1):
        # 이미 죽은 산타 넘기기
        if santas[s]['die']:
            continue
        all_santa_die = False
        santa = santas[s]['locate']
        dis = distance(roo,santa)

        # 거리가 최소보다 더 가깝다면
        if min_dis > dis:
            min_dis = dis
            near_santa = s
        # 거리가 같을때
        elif min_dis == dis:
            # r 좌표가 더 큰 산타
            if maxi < santa[0]:
                maxi = santa[0]
                near_santa = s
            # r 좌표가 동일하다면
            elif maxi == santa[0]:
                # c 좌표가 더 큰 산타
                if maxj < santa[1]:
                    maxj = santa[1]
                    near_santa = s

    # 모든 산타가 죽은 상태면 게임 종료
    if all_santa_die:
        return
    print('가장 가까운 산타',near_santa)
    near_santa_locate = santas[near_santa]['locate']
    min_dir_dis = N*N*2
    # 최종 방향 저장
    final_dir = [0,1]
    # 8방향중 가장 가까워지는 방향 선택
    for di, dj in roo_dir:
        ni = roo[0] + di
        nj = roo[1] + dj
        # 새로운 위치와 가장 가까운 산타의 거리
        dis = distance([ni,nj],near_santa_locate)
        # 거리가 더 가깝다면 움직일 위치를 고침
        if min_dir_dis > dis:
            min_dir_dis = dis
            final_dir[0] = di
            final_dir[1] = dj
    print('움직일 방향',final_dir)
    # 루돌프 위치 변경
    board[roo[0]][roo[1]] = 0
    roo[0] += final_dir[0]
    roo[1] += final_dir[1]
    board[roo[0]][roo[1]] = 'R'
    # 만약 이동한 위치가 산타한테 도달했다면
    if roo == near_santa_locate:
        roo_hit_santa(near_santa,final_dir)


    for p in range(1,P+1):
        print(santas[p])
        santa_move(p)


def santa_move(num):
    print(num,'번째 산타가 턴을 돕니다')
    # 기절 유지 시간이 남았다면 1턴 줄여주고 넘기기
    if santas[num]['is_faint'] > 0:
        santas[num]['is_faint'] -= 1
        print('기절한 산타입니다')
        return
    # 죽으면 넘기기
    elif santas[num]['die']:
        print('즉은 산타입니다')
        return
    else:
        for i in range(N):
            print(board[i])
        min_dis = N*N*2
        can_go = False
        is_meet = False
        final_dir = santa_dir[0]
        for di, dj in santa_dir:
            ni = santas[num]['locate'][0] + di
            nj = santas[num]['locate'][1] + dj
            # 범위안에 있다면
            if 0<=ni<N and 0<=nj<N:

                # 다른 산타가 있으면 넘기기
                if board[ni][nj] != 0 and board[ni][nj] != 'R':
                    continue
                can_go = True
                # 만약 루돌프라면
                if board[ni][nj] == 'R':
                    is_meet = True
                    min_dis = 0
                    final_dir = [di,dj]
                    break
                else:
                    dis = distance([ni,nj],roo)
                    if min_dis > dis:
                        min_dis = dis
                        final_dir = [di,dj]

        # 루돌프를 만났다면
        if is_meet:
            print('산타가 루돌프를 쳤습니다!')
            # 튕겨져 나감
            board[santas[num]['locate'][0]][santas[num]['locate'][1]] = 0
            santas[num]['locate'][0] += final_dir[0]*(-1)*D
            santas[num]['locate'][1] += final_dir[1] * (-1) * D
            santas[num]['point'] += D
            si = santas[num]['locate'][0]
            sj = santas[num]['locate'][1]
            # 범위 안에 있다면
            if 0<=si<N and 0<=sj<N:
                other = board[si][sj]
                board[si][sj]= num
                if other != 0:
                    santa_hit_santa(other,final_dir)
                    return
            else:
                santas[num]['die'] = True
        # 갈 수 있는 방향이 있다면
        elif is_meet == False and can_go:
            print('최종 방향',final_dir)
            print('가기전 위치',santas[num]['locate'])
            si = santas[num]['locate'][0] + final_dir[0]
            sj = santas[num]['locate'][1] + final_dir[1]

            if 0<=si<N and 0<=sj<N and board[si][sj] == 0:
                board[santas[num]['locate'][0]][santas[num]['locate'][1]] = 0
                board[si][sj] = num
                santas[num]['locate'][0] = si
                santas[num]['locate'][1] = sj
                return


def roo_hit_santa(santa,dir):
    print('루돌프가 산타를 쳤습니다!')
    print('roo',roo,'santa',santas[santa]['locate'])
    di = dir[0]
    dj = dir[1]
    # 루돌프가 움직여서 충돌이 일어난 경우,
    # 해당 산타는 C만큼의 점수를 얻게 됩니다.
    santas[santa]['point'] += C
    # 두턴만큼 기절
    santas[santa]['is_faint'] = 2
    # 이와 동시에 산타는 루돌프가 이동해온 방향으로
    # C 칸 만큼 밀려나게 됩니다.
    santas[santa]['locate'][0] += C*di
    santas[santa]['locate'][1] += C*dj

    si = santas[santa]['locate'][0]
    sj = santas[santa]['locate'][1]
    # 밀려난 위치가 보드 밖일 경우 죽음
    if not(0<=si<N and 0<=sj<N):
        santas[santa]['die'] = True
        return
    else:
        other = board[si][sj]
        board[si][sj] = santa
        # 빈칸이 아니라면(산타가 있는곳)
        if other != 0:
            santa_hit_santa(other,dir)


def santa_hit_santa(damage,dir):
    print('산타가 산타를 쳤습니다!')
    print('santa', santas[damage]['locate'],'방향',dir)
    # 딕셔너리 정보 바꾸기
    santas[damage]['locate'][0] += dir[0]
    santas[damage]['locate'][1] += dir[1]

    si = santas[damage]['locate'][0]
    sj = santas[damage]['locate'][1]

    # 밀려난 위치가 보드 밖일 경우 죽음
    if not (0 <= si < N and 0 <= sj < N):
        santas[damage]['die'] = True
        return
    other_santa = board[si][sj]
    board[si][sj] = damage
    # 밀려난 위치가 다른 산타라면,, 연쇄작용
    if other_santa != 0:
        santa_hit_santa(other_santa,dir)
        return





roo_dir = [[-1,-1],[-1,0],[-1,1],[0,-1],[0,1],[1,-1],[1,0],[1,1]]
santa_dir = [[-1,0],[0,1],[1,0],[0,-1]]


N,M,P,C,D = map(int,input().split())
# N: 게임판의 크기 (3≤N≤50)
# M: 게임 턴 수 (1≤M≤1000)
# P: 산타의 수 (1≤P≤30)
# C: 루돌프의 힘 (1≤C≤N)
# D: 산타의 힘 (1≤D≤N)
board = [[0]*N for _ in range(N)]
roo = list(map(int,input().split()))
roo[0] -= 1
roo[1] -= 1
board[roo[0]][roo[1]] = 'R'
santas = {}
for s in range(P):
    num,r,c = list(map(int,input().split()))
    santas[num] = {
        'locate':[r-1,c-1],
        'is_faint': 0,
        'die': False,
        'point':0,
    }
    board[r-1][c-1] = num
print('시작')
print(santas)
print('roo',roo)
for i in range(N):
    print(board[i])
for m in range(M):
    all_santa_die = True
    order()
    print(santas)
    print('roo', roo)
    print(m+1,'번째 턴')
    for i in range(N):
        print(board[i])
    print()
    # 모든 산타가 죽었으면 종료
    if all_santa_die:
        break


for s in range(1,P+1):
    # 안죽은 산타 1점 추가부여
    if santas[s]['die'] == False:
        santas[s]['point'] += 1
    print(santas[s]['point'],end=' ')
print()
