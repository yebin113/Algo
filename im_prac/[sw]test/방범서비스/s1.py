import sys
import pprint
# 보류

sys.stdin = open('input.txt')


# 운영비용 구해주는 함수
def pay(size):
    money = size * size + (size - 1) * (size - 1)
    return money


def grain(arr, i, j, M):  # 배열과 위치와 범위
    visited = [[0]*N for i in range(N)]
    sum_arr1 = 0
    sum_arr2 = 0
    # 1. 위의 마름모, 아래 마름모 비교할것
    # 가운데 줄 먼저 더해줌
    for k in range(-M + 1, M):
        # 만약 현재 위치가 범위안에 있다면
        if 0 <= i - (M - 1) < N and 0 <= j + k < N:
            sum_arr1 += arr[i - (M - 1)][j + k]
            visited[i - (M - 1)][j + k] = '가운데'
        if 0 <= i + (M - 1) < N and 0 <= j + k < N:
            sum_arr2 += arr[i + (M - 1)][j + k]
            visited[i + (M - 1)][j + k] = '가운데'
    print(M)
    pprint.pp(visited)
    # 정중앙에서 계단모양으로 넓어지면서 더해줌
    # 열은 중간줄을 제외하고 M-1번 수행
    for k in range(M-1):
        # 행은 M-1-k의 위치 양옆을 더해줌
        for l in range(-M+2, M-1):
            # 범위 밖일때 그냥 넘어가줌..
            if 0<=i-k<N and 0<= j+l+k-(M-2) <N:
                # 열의 인덱스 범위는 시작점: i 부터 중간아래줄 : i-(M-2) 까지
                # 행의 인덱스는 중간 j를 기점으로 -(M-2-k) ~ (M-2-k)
                sum_arr1 += arr[i-k][j+l+k-(M-2)]
                visited[i-k][j+l+k-(M-2)] = 1
            if 0<=i+k<N and 0<= j+l+k-(M-2) <N:
                sum_arr2 += arr[i+k][j+l+k-(M-2)]
                visited[i+k][j+l+k-(M-2)] = 2

            if 0<=i-M-k<N and 0<= j+l-k <N:
                # 중간윗줄 : i-M 부터 끝점 : i-2(M-1) 까지
                sum_arr1 += arr[i-M-k][j+l-k]
                visited[i-M-k][j+l-k] = 1

            if 0<=i+M+k<N and 0<= j+l-k <N:
                sum_arr1 += arr[i+M+k][j+l-k]
                visited[i+M+k][j+l-k] = 2


    pprint.pp(visited)
    return max(sum_arr1,sum_arr2)

T = int(input())
for tc in range(1, T + 1):
    # 도시의 크기 N과 하나의 집이 지불할 수 있는 비용 M
    N, M = map(int, input().split())
    # N*N 크기의 도시정보가 주어진다. 지도에서 1은 집이 위치한 곳이고, 나머지는 0
    arr = [list(map(int, input().split())) for i in range(N)]
    max_size = 0
    # m = 보안 사이즈
    for m in range(N//2, -1, -1):
        # i = 열순회
        for i in range(2):
            # j = 행 순회
            for j in range(2):
                # 각 배열을 한칸씩 순회하면서
                home_count = grain(arr,i,j,m)

                # 집들이 내는 돈 > 보험회사 운영비용일때
                # 그리고 최댓값 갱신
                if home_count * M > pay(m) and max_size < home_count:
                    max_size = home_count

    print(f'#{tc} {max_size}')
