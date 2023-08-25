import sys
import pprint

sys.stdin = open('input.txt')


def down(arr, i, j, k):
    # print(f'down 사이즈 {k}')
    """
    :param arr: 배열
    :param i: 현재 열
    :param j: 현재 행
    :param k: 현재 방범 사이즈
    :return: 현재 위치에서
    """
    visited = [[0] * N for i in range(N)]
    cnt = 0
    for ni in range(k):
        for nj in range(j - ni, j + ni + 1):
            if 0 <= i + ni < N and 0 <= nj < N:

                cnt += arr[i + ni][nj]
                # print(f'현재위치 {i + ni} {nj} 집 개수 {cnt}')
                visited[i + ni][nj] += 2
                if ni != k-1 and 0 <= i + 2*(k - 1) - ni < N:

                    cnt += arr[i + 2*(k - 1) - ni][nj]
                    visited[i + 2*(k - 1) - ni][nj] += 2
    return visited,cnt


# 주어진 위치의 위쪽 마름모모양의 집 수를 구하는 함수
def up(arr, i, j, k):
    # print(f'up 사이즈 {k}')
    cnt = 0
    """
    :param arr: 배열
    :param i: 현재 열
    :param j: 현재 행
    :param k: 현재 방범 사이즈
    :return: 현재 위치에서
    """
    visited = [[0] * N for i in range(N)]

    for ni in range(k):
        for nj in range(j - ni, j + ni + 1):
            if 0 <= i - ni < N and 0 <= nj < N:
                visited[i - ni][nj] += 1
                if arr[i - ni][nj] != 0:
                    cnt += 1
                # print(f'현재위치 {i-ni} {nj} 집 개수 {cnt}')
                if ni != k-1 and 0 <= i - 2 * (k - 1) + ni < N:
                    if arr[i - 2 * (k - 1) + ni][nj] != 0:
                        cnt += 1
                    visited[i - 2 * (k - 1) + ni][nj] += 1
    return visited,cnt


def pay(K):
    return K*K+(K-1)*(K-1)


T = int(input())
for tc in range(1, T + 1):
    # 도시의 크기 N과 하나의 집이 지불할 수 있는 비용 M
    N, M = map(int, input().split())
    # N*N 크기의 도시정보가 주어진다. 지도에서 1은 집이 위치한 곳이고, 나머지는 0
    arr = [list(map(int, input().split())) for i in range(N)]
    ans = 0
    max_size = 0

    # 사이즈가 큰쪽에서 작은쪽으로
    for k in range(2*N,-1,-1):
        for i in range(N):
            # 각 위치에서 모두 계산
            for j in range(N):
                # 아래 마름모 집의 수
                cnt1 = down(arr, i, j, k)[1]
                # 위의 마름모 집의 수
                cnt2 = up(arr, i, j, k)[1]
                # 집들이 낼 수 있는 돈과 운영비용의 차 (회사 이익)
                MONEY = max(cnt2,cnt1) * M - pay(k)
                # 만약 서비스 지역의 운영비용보다 현재 집들이 낼수있는 돈이 큰데 사이즈가 더 클 수 있다면?
                if MONEY >= 0 and max_size < k :
                    # 사이즈 갱신
                    max_size = k
                    # 방문한곳 뽑으려고 넣은 코드
                    if max(cnt2,cnt1) == cnt1:
                        arr3 = down(arr, i, j, k)[0]
                    else:
                        arr3 = up(arr, i, j, k)[0]
                    # 최대 집 수도 갱신
                    ans = max(cnt2,cnt1)

    print(f'#{tc} {max_size} {ans} {pay(max_size)}')
    pprint.pp(arr3)
