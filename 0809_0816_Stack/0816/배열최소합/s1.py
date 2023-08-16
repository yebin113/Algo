import sys
sys.stdin = open("input.txt")

T = int(input())



def sunyeul(i, N):
    if i == N: # 순열 완성
        B = A [:]
        sun_list.append(B)

    else:
        for j in range(i,N):        # 자신부터 오른쪽 끝까지
            A[i], A[j] = A[j], A[i]
            sunyeul(i + 1, N)
            A[i], A[j] = A[j], A[i]


def minhap(sun,arr,min_hap):
    # 주어진 순열을 이용해서 겹치지 않는 세로줄의 합을 구함

    hap = 0
    # 열을 돌면서
    for i in range(N):
        # 주어진 순열에 해당하는 칸의 숫자들만 더함
        hap += arr[i][sun[i]]
        # 더하는중에 최솟값보다 커지면 반복문 그만돌림
        if hap > min_hap:
            break






for tc in range(1, T+1):
    # 배열 크기
    N = int(input())
    # 순열 생성할 배열
    A = [i for i in range(N)]
    # N * N 배열
    arr = [list(map(int, input().split())) for i in range(N)]
    min_hap = 10000
    # 0~N-1 에 대한 순열을 생성해보자
    sun_list = []
    sunyeul(0,N)
    # [[0, 1, 2], [0, 2, 1], [1, 0, 2], [1, 2, 0], [2, 1, 0], [2, 0, 1]]

    # 주어진 순열을 이용해서 겹치지 않는 세로줄의 합을 구함
    for sun in sun_list:        # sun -> [0, 1, 2]
        hap = 0
        # 열을 돌면서
        for i in range(N):
            # 주어진 순열에 해당하는 칸의 숫자들만 더함
            hap += arr[i][sun[i]]
            # 더하는중에 최솟값보다 커지면 반복문 그만돌림
            if hap > min_hap:
                break
        # 최솟값 갱신
        if min_hap > hap:
            min_hap = hap



    print(f'#{tc} {min_hap}')