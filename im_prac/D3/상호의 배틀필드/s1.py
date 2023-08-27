import sys
sys.stdin = open("input.txt")
import pprint

def button(play,sti,stj):
    global dir

    for p in range(N):
        if play[p] == 'U':
            # 전차가 바라보는 방향을 위쪽으로 바꾸고, 다음칸은 한칸 위
            dir = 0
            ni = sti - 1
            nj = stj
        elif play[p] == 'D':
            # 전차가 바라보는 방향을 아래쪽으로 바꾸고, 다음칸은 한칸 아래
            dir = 1
            ni = sti + 1
            nj = stj
        elif play[p] == "L":
            # 전차가 바라보는 방향을 왼쪽으로 바꾸고, 다음칸은 한칸 왼쪽
            dir = 2
            ni = sti
            nj = stj - 1
        elif play[p] == 'R':
            # 전차가 바라보는 방향을 오른쪽으로 바꾸고, 다음칸은 한칸 오른쪽
            dir = 3
            ni = sti
            nj = stj + 1
        # 슈팅이라면....
        else:
            # print(f'{play[p]} 포탄을 쏩니다 현재 위치 {sti} {stj}')
            shooti = sti
            shootj = stj
            # 다음 칸이 범위 안에 있을때 까지

            while 0 <= shooti < H and 0 <= shootj < W:
                # 방향이 위쪽이다..
                if dir == 0:
                    shooti -= 1
                    if shooti < 0:

                        break

                # 방향이 아래쪽이다..
                elif dir == 1:
                    shooti += 1
                    if shooti >= H:

                        break

                # 방향이 왼쪽이다..
                elif dir == 2:
                    shootj -= 1
                    if shootj < 0:

                        break

                # 방향이 오른쪽이다..
                else:
                    shootj += 1
                    if shootj > W:

                        break


                # 벽돌로 만들어져있으면 평지로 만들고
                if 0 <= shooti < H and 0 <= shootj < W and field[shooti][shootj] == '*':
                    field[shooti][shootj] = '.'
                    # 포탄 소멸
                    break
                # 강철이면 포탄 파괴..
                elif 0 <= shooti < H and 0 <= shootj < W and field[shooti][shootj] == '#':
                    break
            # 슈팅은 이동 안함
            continue

        # 다음 칸이 범위 안에 있고 평지라면 그 칸으로 이동한다.
        if 0 <= ni < H and 0 <= nj < W and field[ni][nj] == '.':
            # 들렀던 곳은 평지가 되고
            field[sti][stj] = '.'
            # 위치 갱신을 한 뒤
            sti = ni
            stj = nj
            # 이동을 합니다
            field[sti][stj] = tank[dir]

        else:
            # 방향만 바꿉니다...
            field[sti][stj] = tank[dir]

        
T = int(input())

for tc in range(1, T+1):
    tank = ['^','v','<','>']
    H,W = map(int,input().split())
    field = [list(input()) for i in range(H)]
    N = int(input())
    play = list(input())

    # 전차의 위치와 방향 찾기 -> 잘 됨
    for i in range(H):
        for j in range(W):
            if field[i][j] in '^v<>':
                sti = i
                stj = j
                dir = tank.index(field[i][j])
                # print('시작위치',sti,stj,'방향',dir)
                break
    button(play,sti,stj)


    # 게임 맵을 H개의 줄에 걸쳐 출력한다.
    print(f'#{tc}',end=' ')
    for i in range(H):
        for j in range(W):
            print(field[i][j],end='')
        print()