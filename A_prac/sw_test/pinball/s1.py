import sys

sys.stdin = open("input.txt")

T = int(input())

dij = [[0, 1], [1, 0], [-1, 0], [0, -1]]


def play(i, j, dir):
    sti = i
    stj = j
    cnt = 0
    while 0 <= i < N and 0 <= j < N:
        # 방향 get
        di, dj = dij[dir]
        # 새로운 인덱스
        ni = i + di
        nj = j + dj

        # 범위 안 일때
        if 0 <= ni < N and 0 <= nj < N:
            # 시작위치로 돌아오거나 블랙홀 만나면 종료
            if (ni== sti and nj == stj) or arr[ni][nj] == -1:
                return cnt
            # 위치 갱신
            i = ni
            j = nj
            # 1번 블록이라면 (◣)
            if arr[i][j] == 1:
                cnt += 1
                if dir in [1,2]:
                    dir = 3-dir
                else:
                    dir = abs(dir - 2)
            # 2번 블록이라면 (◤)
            elif arr[i][j] == 2:
                cnt += 1
                if dir in [2,3]:
                    dir = 5-dir
                else:
                    dir = abs(4-dir)
            # 3번 블록이라면(◥)
            elif arr[i][j] == 3:
                cnt += 1
                if dir in [0,3]:
                    dir = abs(dir-3)
                elif dir == 1:
                    dir = 3
                else:
                    dir = 0

            # 4번 블록이라면 (◢)
            elif arr[i][j] == 4:
                cnt += 1
                if dir in [0,1]:
                    dir = abs(dir-1)
                else:
                    dir = dir -2

            # 네모 블럭 ■
            elif arr[i][j] == 5:
                cnt += 1
                # 반전시켜주기
                if dir in [0, 2]:
                    dir += 1
                else:
                    dir -= 1
            elif 6 <= arr[i][j] <= 10:
                # 만약 웜홀이라면 같은 값을 가진 다른 웜홀로 나옴
                flag = False
                for k in range(N):
                    for m in range(N):
                        if [k, m] != [i, j] and arr[k][m] == arr[i][j]:
                            i = k
                            j = m
                            flag = True
                            break
                    if flag:
                        break
                # 벽에 부딫힐때..
            else:


    return cnt


for tc in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for i in range(N)]
    max_cnt = 0
    # 시작할 수 있는 위치 찾기
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 0:
                # 해당 위치에서 시작해서 벽에 부딫힌 횟수 리턴받기
                cnt1 = play(i, j, 0)
                cnt2 = play(i, j, 1)
                cnt3 = play(i, j, 2)
                cnt4 = play(i, j, 3)
                # 최댓값 갱신
                if max_cnt < max(cnt4, cnt3, cnt1, cnt2):
                    max_cnt = max(cnt4, cnt3, cnt1, cnt2)
    print(f'#{tc}')
