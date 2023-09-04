import sys

sys.stdin = open("input.txt")


def rotate(magnet, dir):
    # 범위 나가면 리턴
    if magnet < 0 or magnet > 3:
        return
    # 일단 새로운 방향 제시(거꾸로)
    if dir == -1:
        new_dir = 1
    elif dir == 1:
        new_dir = -1
    else:
        new_dir = 0
    # 자석이 3이 안넘고, 양쪽이 다를때
    if magnet < 3 and arr[magnet][2] != arr[magnet + 1][6]:
        # 새로운 방향에 추가
        dir_list[magnet + 1] = new_dir
    # 자석이 3이 안넘고, 양쪽이 같을때
    elif magnet < 3 and arr[magnet][2] == arr[magnet + 1][6]:
        new_dir = 0
        dir_list[magnet + 1] = new_dir

    # 재귀
    rotate(magnet + 1, new_dir)

    if magnet > 0 and arr[magnet][6] != arr[magnet - 1][2]:
        dir_list[magnet - 1] = new_dir

    # 자석이 3이 안넘고, 양쪽이 같을때
    elif magnet < 3 and arr[magnet][2] == arr[magnet - 1][6]:
        new_dir = 0
        dir_list[magnet - 1] = new_dir
    rotate(magnet - 1, new_dir)


# 진짜 돌려줌
def real_rocate(dir_list):
    for i in range(4):
        # 반시계방향
        if dir_list[i] == -1:
            zero = arr[i].pop()
            arr[i].insert(0, zero)
        # 시계방향
        elif dir_list[i] == 1:
            zero1 = arr[i].pop(0)
            arr[i].append(zero1)


T = int(input())

for tc in range(1, T + 1):
    # 자석 회전 정보 K
    K = int(input())
    # 자석의 자성정보
    arr = [list(map(int, input().split())) for i in range(4)]
    # 회전시키려는 자석의 번호, 회전방향
    # 각 자석의 날 자성정보는 빨간색 화살표 위치의 날부터 시계방향 순서대로
    # 회전방향은 1 일 경우 시계방향이며, -1 일 경우 반시계방향
    for i in range(K):
        magnet, dir = map(int, input().split())
        magnet -= 1
        dir_list = [0] * 4
        dir_list[magnet] = dir
        rotate(magnet, dir)
        real_rocate(dir_list)
    ans = 0
    for i in range(4):
        #  N 극이 0 으로, S 극이 1
        if arr[i][0] == 1:
            ans += 2 ** i
    print(f'#{tc} {ans}')
