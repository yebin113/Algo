import sys
sys.stdin = open("input.txt")

T = int(input())


# 갈 수 있는 방의 수
def find_cnt(i,j):
    cnt = 0
    while 1:
        # print(f'위치 {i} {j} 현재 숫자 {arr[i][j]}  카운트 {cnt}')
        cnt += 1
        # 오른쪽으로 갈때
        # 오른쪽이 범위 안에 있고, 오른쪽이 1 높은 방일때
        if j + 1 < N and arr[i][j+1] == arr[i][j]+1:
            j += 1
        # 아래쪽이 범위안에 있고 아래쪽이 1 높은 방일때
        elif i + 1 <N and arr[i+1][j] == arr[i][j]+1:
            i += 1
        # 왼쪽이 범위안에 있고 왼쪽이 1 높은 방일때
        elif 0 <= j -1 and arr[i][j-1] == arr[i][j]+1:
            j -= 1
        # 위쪽이 범위안에 있고 위쪽이 1 높은 방일때
        elif 0 <= i - 1 and arr[i-1][j] == arr[i][j]+1:
            i -= 1
        else:
            return cnt



for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for i in range(N)]
    max_cnt = 0
    min_num = N*N*N
    arr2 = []
    for i in range(N):
        for j in range(N):
            cnt = find_cnt(i,j)
            if max_cnt < cnt:
                # print(f'이전의 카운트 {max_cnt} 바뀔 카운트 {cnt}')
                max_cnt = cnt
                min_num = arr[i][j]
            if max_cnt == cnt:
                max_cnt = cnt
                if min_num > arr[i][j]:
                    # print(f'이전의 값 {min_num} 바뀔 값 {arr[i][j]}')
                    min_num = arr[i][j]



    # 처음에 출발해야 하는 방 번호와 최대 몇 개의 방을 이동할 수 있는지
    print(f'#{tc} {min_num} {max_cnt}')