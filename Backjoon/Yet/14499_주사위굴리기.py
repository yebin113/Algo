direction = {
    1:[0,1],
    2:[0,-1],
    3:[-1,0],
    4:[1,0]
}

dice = {
    'up':0,
    'down':0,
    'left':0,
    'right':0,
    'front':0,
    'back':0
}

def turn(dir):
    """
    주사위 굴리기
    :param dir: 주사위를 굴릴 방향
    """
    up = dice['up']
    down = dice['down']
    left = dice['left']
    right = dice['right']
    front = dice['front']
    back = dice['back']
    if dir == 1: # 동
        dice['up'] = left
        dice['down'] = right
        dice['left'] = down
        dice['right'] = up
    elif dir == 2: # 서
        dice['up'] = right
        dice['down'] = left
        dice['left'] = up
        dice['right'] = down
    elif dir == 3: # 북
        dice['up'] = front
        dice['down'] = back
        dice['front'] = down
        dice['back'] = up
    elif dir == 4: # 남
        dice['up'] = back
        dice['down'] = front
        dice['front'] = up
        dice['back'] = down

def copy_m_d(nowx,nowy):
    """
    칸에 쓰여 있는 수가 0이면, 주사위의 바닥면에 쓰여 있는 수가 칸에 복사
    0이 아닌 경우에는
    칸에 쓰여 있는 수가 주사위의 바닥면으로 복사되며, 칸에 쓰여 있는 수는 0이 된다.
    :param nowx, nowy: 주사위 현재 위치
    """
    if maps[nowx][nowy] == 0:
        maps[nowx][nowy] = dice['down']
    else:
        dice['down'] = maps[nowx][nowy]
        maps[nowx][nowy] = 0



N,M,x,y,K = map(int,input().split())
maps = [[0]*M for _ in range(N)]
for i in range(N):
    map_info = list(map(int,input().split()))
    for j in range(M):
        maps[i][j] = map_info[j]

order = list(map(int,input().split()))
copy_m_d(x,y)
for i in range(K):
    dx = direction[order[i]][0]
    dy = direction[order[i]][1]

    x += dx
    y += dy
    if x < 0 or y < 0 or x >= N or y >= M:
        x -= dx
        y -= dy
        continue
    turn(order[i])
    copy_m_d(x, y)
    print(dice['up'])