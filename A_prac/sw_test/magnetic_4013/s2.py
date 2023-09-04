import sys

sys.stdin = open("input.txt")


# 돌려줌
def rocate(dir_list):
    for i in range(4):
        # 반시계방향
        if dir_list[i] == 1:
            zero = arr[i].pop()
            arr[i].insert(0, zero)
        # 시계방향
        elif dir_list[i] == -1:
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
        # 자석 인덱스로 주기
        dir_list = [0]*4
        # 자석정보는 인덱스로 만들어줌
        magnet -= 1
        # 현재의 방향 정보를 현재 인덱스에 저장
        dir_list[magnet] = dir
        # 오른쪽으로 갈거 카피
        magnet_r = magnet
        # 왼쪽으로 갈거 카피
        magnet_l = magnet
        # 오른쪽 끝까지 가거나 방향이 0이 아닐때 까지
        while magnet_r < 3 and dir != 0:
            # 오른쪽으로 한칸 이동
            magnet_r += 1
            # 극이 다르다면
            if arr[magnet_r - 1][2] != arr[magnet_r][6]:
                # 방향을 반대로 바꿔주고
                dir = (-1) * dir
                # 현재의 방향리스트에 넣어줌
                dir_list[magnet_r] = dir

            else:
                # 아니면 방향이 0
                dir = 0
        # 방향은 다시 처음 위치로 돌려줌
        dir = dir_list[magnet]
        # 왼쪽 끝까지 가거나 0이 아닐때까지
        while magnet_l > 0 and dir != 0:
            # 왼쪽으로 한칸 가기
            magnet_l -= 1
            # 왼쪽 자석이 극이 다르다면
            if arr[magnet_l][2] != arr[magnet_l+1][6]:
                # 방향을 다른 방향으로 바꿔주고
                dir = (-1) * dir
                # 현재의 방향리스트에 넣어줌
                dir_list[magnet_l] = dir
            else:
                # 극이 같으면 방향은 0
                dir = 0
        # 그리고 모든 방향 기록이 끝난 뒤, 돌려줌
        rocate(dir_list)

    # 모든 돌리기가 끝난 뒤
    # 누적 점수 구하기
    ans = 0
    # 4개의 자석을 돌며
    for i in range(4):
        # S 극이 1이니 1이라면 해당 인덱스의 2의 제곱수 만큼 점수를 얻는다
        if arr[i][0] == 1:
            ans += 2 ** i
    print(f'#{tc} {ans}')
