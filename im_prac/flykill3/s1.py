import sys

sys.stdin = open("input.txt")

# +자
di1 = [0, 0, -1, 1]
dj1 = [-1, 1, 0, 0]

# X자
di2 = [-1, 1, -1, 1]
dj2 = [-1, 1, 1, -1]

T = int(input())

for tc in range(1, T + 1):
    # 배열 크기와 스프레이 범위
    N, M = map(int,input().split())
    arr = [list(map(int, input().split())) for i in range(N)]
    kill_fly_max = 0
    for i in range(N):
        for j in range(N):
            kill_fly1 = arr[i][j]
            kill_fly2 = arr[i][j]
            for k in range(4):
                for m in range(1,M):
                    # +자 인덱스
                    ni1 = i + m * di1[k]
                    nj1 = j + m * dj1[k]
                    # X 자 인덱스
                    ni2 = i + m * di2[k]
                    nj2 = j + m * dj2[k]
                    # 벽세우기
                    if 0<=ni1<N and 0<=nj1<N:
                        # 합
                        kill_fly1 += arr[ni1][nj1]
                    if 0<=ni2<N and 0<=nj2<N:
                        kill_fly2 += arr[ni2][nj2]
            # 갱신
            if kill_fly_max < kill_fly1 :
                kill_fly_max = kill_fly1
            if kill_fly_max < kill_fly2 :
                kill_fly_max = kill_fly2
    print(f'#{tc} {kill_fly_max}')
