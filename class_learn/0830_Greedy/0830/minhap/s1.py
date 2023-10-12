import sys
sys.stdin = open("input.txt")

T = int(input())


def sunyeul(i, M, K):
    global min_hap
    """
    :param i: 현재 위치
    :param M: 배열의 전체 개수
    :param K: 배열의 절반 (1이 K개 들어가야함)
    """
    if i == K:      # 1이 K개 들어갔다면
        # 순열 완성
        ni = 0      # 시작점
        nj = 0
        hap = arr[ni][nj]   # 맨 첫번째 더하고 시작
        for m in range(len_sun):    # 만들어진 순열을 순회하면서
            if sun[m]:      # 만약 1이면
                ni += 1     # i 방향으로 1 가기
            else:           # 아니면
                nj += 1     # j 방향으로 1 가기
            hap += arr[ni][nj]  # 도착까지 더함
            # 가지치기
            if hap > min_hap:
                break
        # 최소 갱신
        if min_hap > hap:
            min_hap = hap

    else:   # K개를 선택하지 않았다면
        for j in range(i,M):    # 순열을 순회하면서
            # 만약 아직 1이 아니라면
            if sun[j] == 0:
                sun[j] = 1  # 1로 만들고
                sunyeul(i+1,M,K)    # 다음칸 재귀
                sun[j] = 0  # 다시 0으로 돌려놓기



for tc in range(1, T+1):
    # N * N 배열
    N = int(input())
    arr = [list(map(int, input().split())) for i in range(N)]
    sun_set = []
    len_sun =  2 * N -2
    # 1과 0으로 갈 위치를 정할것
    sun = [0] * len_sun
    min_hap = 1000000000
    sunyeul(0,len_sun,len_sun//2)

    print(f'#{tc} {min_hap}')